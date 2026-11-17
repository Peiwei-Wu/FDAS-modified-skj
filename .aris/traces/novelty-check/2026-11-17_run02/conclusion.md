# Problem-level novelty decision

Decision: PROCEED WITH CAUTION. Prior run01 positioning must be narrowed by IFND and FNC evidence. No claim that the general insight is new.

Claims checked:

1. Content provenance is not semantic class identity; reliable source-positive and semantically screened negatives: explicitly anticipated by FNC (WACV2022) and IFND (ICLR2022).
2. Global K-means pseudo labels, same-cluster false-negative elimination, no forced semantic-positive attraction: IFND Sections3.2–3.3 Eq3 and discussion of noisy attraction are direct prior art.
3. Region mixing plus source-consistent contrast for segmentation pretraining: RegionCL (ECCV2022) and CP2 (ECCV2022) are close; checked formulations use source-driven contrast, rather than shared pseudo-class screening.

Bounded remaining delta: Track the retained and pasted regions of a cross-patient composite to their actual source regions, then organize regional supervision by the source images' pseudo classes; do not equate different origins with different tissues. This is a targeted integration/extension, not a new general principle of contrastive learning.

New primary sources read:
- https://openaccess.thecvf.com/content/WACV2022/html/Huynh_Boosting_Contrastive_Self-Supervised_Learning_With_False_Negative_Cancellation_WACV_2022_paper.html (abstract; PDF access failed)
- https://arxiv.org/html/2106.03719 (intro, related work, Sections3.2–3.3, attraction/elimination findings)
- https://www.cs.jhu.edu/~alanlab/Pubs22/wang2022cp2.pdf (Section3.1, appendix masking comparison)
- https://arxiv.org/abs/2111.15454 (served fulltext: class-/instance-level mixing, AppendixA.4; formal venue not verified)

Search coverage: source consistency, source correspondence, semantic identity, region mixing, false negative, K-means; 2025–2026 and past183days arXiv/CVF/MICCAI/OpenReview queries. No exact full-chain duplicate found within this search. Not an exhaustive non-existence claim. No training code modified.
