const TASK_ID = "SYN-GAS-001";
const HANDLER_NAME = "runSyntheticQualificationWorker";

function startSyntheticQualification() {
  const triggers = ScriptApp.getProjectTriggers();
  const properties = PropertiesService.getScriptProperties();
  if (triggers.length !== 0 || Object.keys(properties.getProperties()).length !== 0) {
    throw new Error("Unexpected existing trigger or property; stopping without changes.");
  }
  properties.setProperty("task_id", TASK_ID);
  ScriptApp.newTrigger(HANDLER_NAME).timeBased().after(60000).create();
  return { task_id: TASK_ID, phase: "scheduled", sample_only: true };
}

function runSyntheticQualificationWorker() {
  const properties = PropertiesService.getScriptProperties();
  if (properties.getProperty("task_id") !== TASK_ID) {
    throw new Error("Synthetic task marker missing; stopping.");
  }
  properties.setProperty("trigger_fired", "true");
}

function finalizeSyntheticQualification() {
  const properties = PropertiesService.getScriptProperties();
  const fired = properties.getProperty("trigger_fired") === "true";
  const testTriggers = ScriptApp.getProjectTriggers().filter(
    (trigger) => trigger.getHandlerFunction() === HANDLER_NAME
  );
  testTriggers.forEach((trigger) => ScriptApp.deleteTrigger(trigger));
  const triggerRemoved = ScriptApp.getProjectTriggers().every(
    (trigger) => trigger.getHandlerFunction() !== HANDLER_NAME
  );
  const receipt = {
    task_id: TASK_ID,
    status: fired && triggerRemoved ? "complete" : "blocked",
    sample_only: true,
    files_read: ["Code.gs", "appsscript.json"],
    files_changed: [],
    checks: [
      { name: "one-time-trigger-fired", result: fired ? "passed" : "failed" },
      { name: "test-trigger-cleaned-up", result: triggerRemoved ? "passed" : "failed" }
    ],
    review_status: "pending"
  };
  properties.deleteAllProperties();
  return receipt;
}

function cleanupSyntheticQualification() {
  ScriptApp.getProjectTriggers()
    .filter((trigger) => trigger.getHandlerFunction() === HANDLER_NAME)
    .forEach((trigger) => ScriptApp.deleteTrigger(trigger));
  PropertiesService.getScriptProperties().deleteAllProperties();
  return { task_id: TASK_ID, cleanup: "complete" };
}