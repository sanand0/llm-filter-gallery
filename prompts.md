# Prompt - Image Filter Discovery

## What CLI tools help with image filtering techniques?

What CLI tools are best for "filter"-like image editing techniques, e.g. a graffiti effect or an embroidery effect? ImageMagick, FFmpeg, or even Pillow (Python) are standard ones. Are there specialized tools? Are there techniques / libraries particularly suited for this?

<!-- https://gemini.google.com/app/c788548f2bc44532 -->

**ANS**: ImageMagick, Fred's ImageMagick Scripts, GMIC.

## AI Coding Agent selection

I want an AI coding agent to continuously discover new image editing techniques, e.g. a graffiti effect or an embroidery effect - something that can be created through a series of filters via Python/JS/... programs or ImageMagick or FFmpeg or any such tools. (In fact, part of the discovery is about what CLI tools can create interesting, innovative new filters.)

The main agent take a set of standard images and guide sub-agents to create a specific filter and execute it on the standard images; then evaluate the output, see if it is apt/good enough and innovative enough, and if required, prompt the sub-agent to improve it further. If the sub-agent does not continuously improve, then it would give up on that trail and move on to the next innovative idea that it has, spawning another sub-agent to deliver that, and so on, for two or three dozen such creative techniques.

These can execute in parallel. The sub-agents' commands (to generate the filter), output, and feedback should be logged to create a story on the process.

I'd like you to research which coding harness would be most suitable for this. Should I use Claude Code, GitHub Copilot, Codex CLI, Antigravity, something else? Think about what's required in terms of capabilities from the description above. These tools are evolving rapidly, so evaluate the latest versions against these, and guide me on what to pick and why.

<!--
https://gemini.google.com/app/639f1dc4adb81655
https://chatgpt.com/c/69956c1e-7e38-83a8-89ae-6276408d921b
-->

**ANS**: Use Claude Code

## Ask what I should do

My aim is to deliver a talk that provokes people into thinking about the creative discovery capability of LLMs. I'd like to show how LLMs can discover new image filters. We already have a whole bunch of image magic filters from Fred. We already have capabilities from GMIC. How should I think about this? Would it be better to extend Fred's filters and show how new filters can be created automatically and that some of them may be of good quality? Should we talk about stacking techniques, like how AI can figure out how to interestingly combine different toolkits to come up with something new or something else? Also, should we explore this as generic techniques that could apply to a large class of images or any image, or should we contextualize this and say, for a given image, AI is able to figure out what are different representations based on different objectives? Which of these are more powerful and why? I'm conscious that these are not mutually exclusive. So I'd like you to research what AI can do currently and in the foreseeable future. Think about how humans are likely to use AI for creative discovery and, based on that, think about the different ways in which I could demonstrate such capability, including the ways that I described, and evaluate these approaches and suggest the top two or three approaches to me with reason.

**ANS**: _Evolutionary Explorer_: Apply a filter, ask for feedback, iterate. Also, _Semantic Translator_: Convert a "vibe" to a code snippet.

## Ask for a generation prompt

For the Evolutionary Explorer, I would like to take an image, pass it to an LLM, and ask it to suggest 3 interesting, useful aesthetics to apply to that image and share the code for that. Suggest a crisp prompt for this.

## Ask for a validation prompt

Once I have the output, I would like to pass it to a vision model to evaluate it. What is the best vision model for this purpose? Compare all the latest models and recommend the top 3 with reason.

What prompt should I pass it so that I can get the results in a comparable form across images? Keep in mind that we would need some kind of a semantic rating to be able to compare across images because the LLM will not have any anchoring otherwise.

## Generate the images (Claude Code, Sonnet 4.6)

Act as a world-class Aesthetic Architect. Generate 3 brand-new, sophisticated, and aesthetically distinct 'Signature Filters' for inputs/chart.avif with:

1. **Combinatorial Creativity:** Prefer multi-step filters. A filter is a _recipe_.
2. **Distinct Moods:** The 3 filters must look completely different from each other.
3. **Naming:** Give each filter an evocative name.
4. **Tech Stack:** You can use magick, Fred's imagemagic filters in bin/, GMIC, Python (NumPy/PIL/OpenCV), cwebp, or any other available tools.

Save the results under `output/chart-claude-code-v{1,2,3}/{README.md,filter.sh,output.webp}` where

- README.md explains the filter and why it's interesting.
- filter.sh has the code to apply the filter.
- output.webp is the (maximally compressed) result of applying the filter to inputs/chart.avif.

## Restructure the directories

Create a filters/ that has each of the filters under `output/*/filter.sh`.
Name them in line with index.html, e.g. `filters/graphite-study.sh`.
Include `filters/graphite-study.md` which is the same as `output/*/README.md` -- ignoring the last line, which is different across the variants.

Move `output/*/output.webp` into `output/$image-$filter-name.webp`, e.g. `output/comic-graphite-study.webp`.

Update index.html accordingly.

## Evaluate quality

### GPT Evaluation (Copilot Yolo, GPT 5.3 Codex xhigh)

Let's evaluate the filters in this repository. Which of these are really good and why?
Think like an artist, as an expert in data art, aesthetics, and visual design.
What would an expert would look for (that a beginner would miss) in these visual effects and filters?
Identify the criteria by searching online for the best researched material around this and augment your trained knowledge.
Imagine that you are a judge judging an art exhibition.
Use those criteria to go through all of the output images and carefully evaluate them against these criteria.
Prepare a scoring table as if such a judge would have created it.
Also include specific feedback (what's good, what's not good) for each of these entries that will support your rationale.
The output should be an `gpt-evaluation.md` that has the scoring table and the feedback for each of the filters.
Remember that you're evaluating at the filter level, not the image level. So if a filter creates a very interesting effect on some images but not others, evaluate that appropriately.

### Claude Evaluation (Copilot Yolo, Sonnet 4.6 High)

Same as above but output is `sonnet-evaluation.md`.

### Gemini Evaluation (Copilot Yolo, Gemini 3 Pro)

Same as above but output is `gemini-evaluation.md`.

### Document process

In the same output file, also document the process you followed to identify the criteria, evaluate the images, and come to the conclusions. This will help in making the process transparent and reproducible.

### Consolidation

Convert \*-evaluation.md into a single structured `evaluation.json` that captures, for each of the three evaluations, the following `evaluations` array of objects with the following fields:

- evaluator: e.g. "gpt", "gemini", "claude" -- from the filename of the evaluation file
- filter-id: e.g. charcoal-on-kraft -- same as the file basename in `filters/`
- name: e.g. "Charcoal on Kraft"
- score: e.g. 0.85 - a number between 0 and 1 that represents the overall quality of the filter based on the evaluation criteria
- feedback: the text feedback for that filter, in Markdown
- criteria: an object with details of the evaluation criteria, e.g. for GPT, {Concept: 0.9, Impact: 0.8, ...} while for claude it could be {"Aesthetic Authenticity": ..., ...} with each criterion having a score between 0 and 1.

This apart, include a `weights` object for each evaluator to calculate the score from the criteria, and any other relevant metadata.

### Synthesize evaluation story (Codex - GPT 5.3 Codex xhigh + Claude Code - Sonnet 4.6)

Using evaluation.json and any other content, write as a **Narrative-driven Data Story** that synthesizes the evaluations into a compelling narrative.

Write like Malcolm Gladwell. Visualize like the NYT graphics team. Think like a detective who must defend findings under scrutiny.

- **Compelling hook**: Start with a human angle, tension, or mystery that draws readers in
- **Story arc**: Build the narrative through discovery, revealing insights progressively
- **Integrated visualizations**: Beautiful, **interactive** charts that are revelatory and advance the story (not decorative)
- **Concrete examples**: Make abstract patterns tangible through specific cases
- **Evidence woven in**: Data points, statistics, and supporting details flow naturally within the prose
- **"Wait, really?" moments**: Position surprising findings for maximum impact
- **So what?**: Clear implications and actions embedded in the narrative
- **Honest caveats**: Acknowledge limitations without undermining the story

The objective is to help the reader understand how we prompted each model (see prompts.md), how each model evaluated the images (see \*-evaluation.md), and what the results were (see evaluation.json). The narrative should weave these elements together to tell a cohesive story about the evaluation process and its findings.

Beauty and aesthetics are key.

Create this as a single evaluation-codex.html that loads evaluation.json and renders the narrative.

### Enrich evaluation story (Claude Code - Sonnet 4.6)

Extensively link to sources - e.g. filters, images, evaluation .md files, etc.
When linking to images, they should appear on a modal popup with captions.
All image thumbnails should also be clickable to view the full image in a modal popup with captions.
In Act II, ensure that the cards for GPT, Claude Sonnet and Gemini are in a single row, side-by-side.
When hovering over the circles in Claud vs GPT Scores - Colored by Gemini, show the output images and rating details on click - in a modal popup.
In the "Terminal Matrix - maximum controversy" card, include two images for Terminal Matrix, just like you've done for Thermal Scan and CMYK Separation.
In The Full Picture sections, clicking on any row should open the filter in a modal popup showing the output images and the evaluation details.
Re-use popup code for consistency and efficiency - i.e. have a single popup "component" for images and one for filters, and re-use it throughout the narrative.
Make the Complete Scores appendix sortable by any column.

---

Allow the cards in Act II to take up more width (.wide)

---

When linking to .md, .sh, or .json files, clicking on them should show them in a popup with a caption and syntax highlighting.

## TODO: Discover

## TODO: Parametrize
