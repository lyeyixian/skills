---
name: writing
description: Write or edit any prose a person reads, in a human voice or in ASD-STE100 Simplified Technical English. Covers replies, docs, procedures, commit messages, PR descriptions, tickets and code comments. Must always apply.
---

# Writing

Prose comes in two registers. **Voice** is plain writing with a person behind it. **Technical** is ASD-STE100 Simplified Technical English. Pick a register for each passage, write by its file, then run the shared rules below over everything.

## Process

1. Pick the register for each passage (next section).
2. Write the passage by that register's file: [unslop.md](unslop.md) for voice, [STE.md](STE.md) for technical. Read the file before the first passage in that register.
3. Scan for the shared rules and fix them.
4. Self-check. Search the draft for `—`, `–`, `“`, `”`, `‘`, `’`, "in order to" and "it is important to note". Fix every hit. Then run the register's check. For voice, ask "What makes this obviously AI generated?" and fix what you find. For technical, run the self-check in STE.md.

## Pick the register

Ask what the reader does with the passage.

- The reader **follows** it or looks something up: technical. Procedures, install and setup steps, runbooks, troubleshooting, CLI and config reference, error and UI messages, warnings, code comments, commit subjects. Also any text for readers who are not native English speakers, or text that goes to translation.
- The reader **weighs** it or wants to understand: voice. Chat replies, explanations, PR descriptions, commit bodies, design docs, proposals, reviews, status updates, posts.

Pick per passage, not per document. A README overview is voice and its install section is technical. A chat reply is voice, and the numbered steps inside it are technical. When a passage could go either way, ask whether the reader acts on each sentence. If yes, use technical.

An explicit request from the user wins: "write it in STE" or "make it sound human".

## Shared rules

These apply in both registers.

### Plain speech

1. **Say what it does, not how it feels.** "the database stays close at hand", "SQL you can read", "types that follow your schema" name a feeling. The fix names the mechanism or a number: "`.toSQL()` returns the exact string sent to the database", "a column rename fails the build". Ask what the sentence tells the reader to do or know, then write that. If you can't restate it as a concrete instruction, fact, or number, cut it. One more check: if the sentence could appear unchanged in another project's docs, it says nothing about this one. Cut it.
2. **Shorten or split dense sentences.** If the reader has to backtrack to parse a sentence, break it in two or drop clauses. One idea per sentence.
3. **Active voice.** Prefer it. Catch "is/are/was/were + past participle" and name the actor: "queries are validated" becomes "the compiler validates queries", "the file is parsed by the loader" becomes "the loader parses the file". Passive is fine only when the actor is unknown or genuinely doesn't matter.
4. **Cut adverbs, or use a stronger verb.** "runs quickly" becomes "is fast" or the number. "significantly improves" becomes the measured delta. An adverb propping up a weak verb means the verb is wrong.
5. **Prefer the plain word.** "utilize" becomes "use", "leverage" becomes "use", "facilitate" becomes "help", "numerous" becomes "many", "in the event that" becomes "if". The fancier synonym is rarely clearer.
6. **One word, one meaning.** Protagonist, main character, central figure, hero all in one paragraph is synonym cycling. Pick one word for each thing and repeat it.
7. **Abstract metaphor nouns.** Substrate, wedge, vector, locus, vantage, nexus, primitive (as noun), harness (as metaphor), surface (as in "API surface"), bedrock, scaffolding (as metaphor), modality, paradigm, gold-plating, ratchet (as metaphor), evacuate (for moving code), endgame, north star, flywheel. These read as technical but usually have a plainer concrete word. "Substrate" becomes "base". "Wedge in" becomes "add". "Vector" becomes "way" or "method". "Gold-plating" becomes "more than the job needs". "Ratchet" becomes the mechanism's real name or "a limit that only tightens". "Evacuate" becomes "move out". "Endgame" becomes "the last phase". Pick the concrete word.

### Filler

8. **Filler phrases.** "In order to" becomes "To". "Due to the fact that" becomes "Because". "It is important to note that" gets deleted.
9. **Excessive hedging.** "could potentially possibly be argued that it might" becomes "may".

### Punctuation and formatting

10. **Em dash overuse.** Avoid em dashes entirely. Use periods or commas only (no parentheses, no en dashes, no hyphen-as-dash substitutes). Em dashes are an AI tell, and reaching for parentheses instead just trades one tell for another. If a thought needs separation, end the sentence or use a comma.
11. **Colon overuse.** Colons are fine before a list or example. Not as mid-sentence connectors. "If you're coming from traditional automation: instead of registering event handlers, you describe conditions" adds nothing with the colon. Rewrite to let the point stand on its own without comparison framing. "Describing when the scheduler should fire works best as plain English." Same meaning, no crutch punctuation.
12. **Boldface overuse.** Don't bold every proper noun or acronym.
13. **Inline-header lists.** The tell is a bold label and colon that restates the line: "**Performance:** Performance improved...". Convert those to prose. A bold lead-in that ends in a period, names the item, and is followed by genuinely new detail ("**Schema in TypeScript.** Tables live in one file.") is fine, not a tell.
14. **Title case headings.** Use sentence case.
15. **Decorative emojis.** Remove from headings and bullets.
16. **Curly quotes.** Replace with straight quotes.
