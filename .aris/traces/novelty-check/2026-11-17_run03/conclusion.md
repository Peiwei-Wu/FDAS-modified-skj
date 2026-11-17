# Final method story — novelty calibration

## Proposed method
Shared SAM-region pseudo-classes organize cross-patient fusion, original-image pseudo-semantic restoration and dual-source region contrast. Exact source-and-spatial correspondence determines positives; actual pseudo-class composition determines admissible per-image/per-class negatives.

## Core claims
1. Shared regional K-means pseudo-label pretraining — closest ALPS, RICE; not independently new.
2. Copy-paste source-region contrast — closest RegionCL, CP²; not independently new. Current positives use exact original-image regions rather than global source-image keys.
3. Pseudo-semantic false-negative screening and class-region keys — closest IFND, RICE OCR, ContrastiveSeg; principles individually known. Current integration uses each pasted region's full class set, single-source/multi-class anchors, per-image/per-class keys, plus restoration of A's original shared labels.

## Closest prior work
- FDAS: structural mask IDs and original/fused global contrast.
- ALPS: SAM features, region K-means labels, segmentation pretraining.
- RegionCL: paste/canvas source-region contrast.
- RICE: semantic region clusters and multi-positive-class exclusion from negative centroids.
- IFND: retain exact augmentation positives while removing same-cluster negatives.
- ContrastiveSeg: per-image/per-class pooled regional keys.

## Assessment
Qualitative novelty score: 6/10 (clear neighbors, specific defensible integration delta; not an empirical result).
Recommendation: PROCEED.
No named checked paper contains the complete configuration. This is a bounded search finding, not proof of universal priority.
Strongest positioning: composition-aware relation construction for cross-patient region fusion, distinguishing content provenance from shared pseudo-class relations.

## Required wording
- Segmentation target is original A's full shared pseudo-label map Y_A, not visible-C labels.
- Contrast follows visible A/B content; restoration follows pre-replacement A.
- Anchors are single-source/multi-class; negative keys are classwise.
- No claim that differing pseudo-labels guarantee differing real organs.
- The FDAS paper's SKD target m'_s differs from the local full-mask target; do not conflate paper and code.
- Do not claim global/local complementarity or per-component first invention.

## Evidence and scope
Main executor checked primary full-method sections of FDAS, ALPS, RegionCL, IFND, RICE and ContrastiveSeg, including recent-paper search in the last six months. Fresh reviewer completed a separate read-only review. Reported reviewer model unavailable; assurance remains provisional.
Training/source code unchanged. Only this review trace was saved.

