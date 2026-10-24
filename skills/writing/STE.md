# Technical (ASD-STE100)

The technical register of the [writing](SKILL.md) skill. The shared rules in SKILL.md still apply.

The reader's attention belongs on the task, so the technical register stays neutral and even. Keep the writer out of it: no opinions, no "I", no rhythm play. Every sentence carries one instruction or one fact.

## Words

- **Use the common word.** "Do", not "perform". "Start", not "initiate". "Make sure", not "ensure". "Show", not "display".
- **Repeat the same word for the same action.** If step 2 says "click", step 5 says "click", never "press" or "select".
- **Copy technical names and facts exactly.** Code, commands, file paths, flags, UI labels, product names, error text and numbers keep their spelling and case: `npm install`, **Save**, `settings.json`.
- **Use only "can", "must" and "will" as modals.** A required "should" becomes "must". Delete an optional "should".
- **Define a term the first time you use it,** in fewer than ten words: "idempotent (safe to run twice)". Product and standard names such as Postgres, S3 and HTTP need no definition.
- **Use single-word verbs.** "Remove", not "take out". "Find", not "look up". "Stop", not "shut down", unless the phrase is the technical name.
- **Keep noun clusters to three words.** "Database connection pool timeout setting" becomes "the timeout setting for the database connection pool".
- **Keep the articles.** "Remove the cover", not "Remove cover". Short sentences come from fewer ideas, not dropped words.
- **Write "-ing" words as clauses.** "Before you install the package", not "Before installing the package". Keep "-ing" only in technical names, such as "logging level".

## Sentences

- **Procedures: 20 words or fewer per sentence.** Descriptions: 25 or fewer.
- **Write instructions in the imperative.** "Run the migration", not "You should run the migration".
- **One instruction per sentence.** Join two actions only when the reader does them at the same time.
- **Put the condition first.** "If the build fails, delete `node_modules`", not "Delete `node_modules` if the build fails".
- **Use simple tenses.** Present, past and future. "The script writes the file", not "the script will have been writing".
- **Use the simple past, not the present perfect.** "The job completed", not "the job has completed".
- **Name what each step depends on:** the host, the flag, or the step before. "Restart the service" becomes "Restart the `sync` service on the host that runs the job."
- **Write two sentences instead of a semicolon.**
- **Use a vertical list** for steps, options, or anything with more than two parts. Number the list when order matters.
- **One topic per paragraph,** six sentences or fewer.
- **Put a warning before the step it applies to.** Start it with the command, then give the reason: "Back up the database before you run the migration. The migration deletes the `users_old` table."

## Self-check

1. Count the words in the three longest sentences. Split each sentence that is over the limit.
2. Search for "should", "may", "might", "has been", "have been", `;` and ", making". Fix every hit.
3. Read each step as a reader with basic English. Make sure that the reader can do the step on the first read.
