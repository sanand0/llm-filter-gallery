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
