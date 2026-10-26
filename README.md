# Tiny Desk AI: Prompt Guide, Shot Timeline, and Audio Alignment

**We built [AI Tiny Desk](https://ai-tinydesk.com/), a paid one-photo concert tool.** This repository shares an original prompt helper, a local audio-alignment script, and measured development notes. It is not the application source, model weights, a music license, or an independent product review.

- [Live web tool](https://ai-tinydesk.com/)
- [Copyable prompt guide](https://ai-tinydesk.com/tiny-desk-ai-prompt/)
- [Creation tutorial](https://ai-tinydesk.com/how-to-make-tiny-desk-ai/)
- [Trend and performance sources](https://ai-tinydesk.com/tiny-desk-ai-trend-explained/)

## Five-shot plan

| Time in accepted sample | Shot | Identity rule |
|---|---|---|
| 0–1.375 s | Opening singer | Uploaded adult portrait |
| 1.375–6.667 s | Keyboard and backing vocals | Fixed fictional band |
| 6.667–13 s | Singer close-up | Same portrait as the opening |
| 13–16.375 s | Saxophone; keyboard in corner | Keep these two people distinct |
| 16.375–19.042 s | Backing group | Reuse the prepared band |

## Build a role-specific instruction

```python
from prompt import lead_instruction
print(lead_instruction("the opening and close-up lead singer", [
    "the keyboard player", "both backing singers", "the saxophonist"
]))
```

For a whole-sequence concept use the shot plan above; split references to satisfy the exact model's limits. A prompt is guidance, not a frame-lock guarantee. Our website uses Seedance 2.0 Mini through EvoLink and assembles prepared band shots with personalized lead segments.

## Local audio alignment

Install FFmpeg yourself, then run:

```bash
python3 mux_audio.py silent-render.mp4 permitted-source.mp4 result.mp4 --offset 0
```

The helper refuses an existing output path, checks for video and audio streams, supports a measured offset when needed, and copies video packets. It does not download any music or include a reference clip. Use input media for which you have the permissions your use requires. The complete current source needs no start offset; measure your own inputs.

## Recorded checks

| Check on October 26, 2026 | Observed result | Evidence scope |
|---|---|---|
| Mixed lead reference, Seedance 2.0 Mini | Close-up replaced; opening still showed the old lead | Developer visual review; not a pass-rate study |
| Isolated opening, first submission | Duration validation failed | Provider status recorded failure; no output |
| Isolated opening, corrected reference | Completed in 116 seconds | Provider reported duration for this one task only |
| 19-second Kling O3 edit experiment | Rejected for input duration | Failed experiment; not our production model |
| Browser audio remux | 459 encoded video packets unchanged in the production fixture | Local accepted-sample comparison; not a buyer transaction |

## Alternatives

| Route | Useful when | Limitation to verify |
|---|---|---|
| Existing editor or CapCut template | You already have permitted media | Template availability, export fees and sound terms |
| General video model | You want to control prompts and references | Model-specific limits and inference costs |
| Dedicated web tool | You want our shown concert workflow | Paid credits, likeness variation, separate music rights |

## Product facts and limits

AI Tiny Desk uses ByteDance Seedance 2.0 Mini through EvoLink for the concert workflow. Standard generation is 480p. The output is approximately 19 seconds in vertical MP4. One credit makes a Standard concert; one-time packs are $9.99 / 1 credit, $19.99 / 3 credits, and $29.99 / 5 credits. Credits do not expire. Confirmed generation failures restore credits, while cash refunds and serious visual defects have separate [refund terms](https://ai-tinydesk.com/refunds).

The current sound version uses performance audio supplied by the site operator including the complete original opening. A silent copy remains available. Buying credits does not grant music rights. We support one consenting adult per input; we do not advertise pet or child support. We do not guarantee exact likeness, a render deadline, search rankings, or that an uploaded photo will pass a model's safety checks.

## Sources and disclosure

We built and operate [AI Tiny Desk](https://ai-tinydesk.com/); this is our own development write-up, not an independent review. Test portraits and our demo band are fictional adults. The tool is independent of NPR, Charlie Wilson, The Gap Band, TikTok, and CapCut. AI assisted the preparation of this write-up; technical statements were checked against our source code and saved test artifacts.

The original performance is [Charlie Wilson's NPR Music Tiny Desk Concert](https://www.youtube.com/watch?v=J3jUEB7qmt8), published June 5, 2023. The artist's [official website](https://www.charliewilsonmusic.com/charlie-wilson-kicks-off-nprs-black-music-month-with-tiny-desk-concert/) identifies Outstanding in the set. This establishes the performance reference, not the identity of the first AI remix creator.
