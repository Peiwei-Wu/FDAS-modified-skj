# Fresh novelty review: provenance versus semantic identity

只读，不修改文件，不生成子代理。中文600字内回答。用户问的不是相似模块，而是是否有人已经提出相同研究问题与insight。不要以自然图/医学、2D/3D等形式差异代替问题层面区别。请独立核查最近邻方法原文，必要时联网读取。

## Proposed idea (author claims, not established results)

FDAS期刊扩展：现有区域引导预训练能够利用结构边界，但跨病例融合后，内容来源与组织类别并不等价。将SAM区域组织为跨病例共享伪语义类别，分别利用来源对应和类别关系指导融合区域学习，使模型兼顾source consistency与semantic discriminability，更适合下游语义分割。

流程：SAM masks->SAM region features->全数据K-means。A的伪类k区域由B同几何位置像素替换。融合C中A保留部分与原A对应位置区域作正，B填入部分与原B对应位置区域作正。依据伪语义选负：不同来源不自动为负，同伪类跨病例不强拉也不推远。拟在A/B两侧按各自原图伪标签分组池化，跨类选择负样本。另有共享伪类分割和C重建A。用户接受伪标签噪声，不要求精确器官标注；勿反复以一器官多簇否定路线。用户报告purity95.7%未给口径，勿当独立核实结果。

## Newly verified close primary sources

1. FNC, Boosting Contrastive Self-Supervised Learning With False Negative Cancellation, WACV2022. https://openaccess.thecvf.com/content/WACV2022/html/Huynh_Boosting_Contrastive_Self-Supervised_Learning_With_False_Negative_Cancellation_WACV_2022_paper.html Abstract明确指出 positives可由同图增强可靠构造，而不同图的negatives忽视语义，提出false-negative elimination/attraction。因此广义的‘source positive/semantic negative’认识已有直接先例。

2. IFND, Incremental False Negative Detection for Contrastive Learning, ICLR2022. https://arxiv.org/html/2106.03719 Sec3.2-3.3用全训练集K-means得到伪类，检测跨图同伪类false negatives；Eq3保留同源增强正对，分母仅收异伪类负；Eq4另比较同伪类额外positives。默认采用elimination；引言及Sec4.4/附录G说明强行吸引对噪声更敏感。精确覆盖‘不强拉跨病例同簇、只剔除负’的一般原则，不能再把该原则当新的发现。

3. CP2, Copy-Paste Contrastive Pretraining for Semantic Segmentation, ECCV2022. https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/2840_ECCV_2022_paper.php ; full text https://www.cs.jhu.edu/~alanlab/Pubs22/wang2022cp2.pdf Sec3.1：相同foreground来源不同增强贴到不同背景；dense contrast把foreground互作正，foreground/background异来源作负；foreground pooled instancecontrast。已做融合来源一致性及面向下游分割，但checked Sec3.1中未使用跨图共享伪类别控制负对。

4. SAMix, Boosting Discriminative Visual Representation Learning with Scenario-Agnostic Mixup, arxiv2111.15454（未核实最终正式venue，不编）. https://arxiv.org/abs/2111.15454 网页显示fulltext。Sec3.1/AppendixA.4已有class-level vs instance-level mixing，online clustering PL，区分inter/intracluster mix，local smoothness+global discrimination。比纯RegionCL再近一步，但不要未经方法全文精读就说它包含同一SAM区域方案。

## Prior turn already checked

5. RegionCL, ECCV2022 https://arxiv.org/abs/2111.12309 ; https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136930468.pdf 用paste/canvas来源作正负，MoCo具体实现为mixed区域与原图全局key配正，来源原则已有，但不是完全相同位置区域对。
6. ALPS https://arxiv.org/pdf/2406.10855 SAMfeatures+globalKmeans+共享伪类+分割预训练，并有医学扩展验证，不应以医学/遥感区别充当新意。
7. SlotCon, NeurIPS2022 https://proceedings.neurips.cc/paper_files/paper/2022/file/6818dcc65fdf3cbd4b05770fb957803e-Paper-Conference.pdf 共享semantic prototypes、same prototype+same image跨增强positives；Eq6后明确其他图所有slots仍为negative。
8. ReCo, ICLR2022 https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/dyson-robotics-lab/ShikunLiu_etal_iclr2022.pdf 类别prototype正对、异类语义负；监督/半监督。
9. UM-SAM, MICCAI2025 https://papers.miccai.org/miccai-2025/paper/2296_paper.pdf SAMmask+DINOfeatures聚类找到特定目标伪标签，随后SAM类别feature/contrastKD，目标是task-specific无监督分割，不是FLARErepresentationpretrain。
10. FDAS原文 https://papers.miccai.org/miccai-2025/paper/2967_paper.pdf Eq9把对应原图作为positive，其余图为negative，区域类别按面积排序。

本轮检索：source consistency/semantic identity/source correspondence/region mixing/false negative/cluster negative；补2025-2026与近183天arxiv、CVF、MICCAI、OpenReview。未找到SAM跨病例融合完整同款，但不是不存在的证明。

请回答：
1. 相同研究问题/insight哪些已经提出？最直接应读哪1-3篇？
2. 当前故事还能否作为扩刊定位？哪句不能再称新？
3. 给一个真正收紧到融合机制的problem statement，不把仅换场景当创新、不故意否定可行组合。

=== NOVELTY VERDICT LIMITS (these bound how you judge, never how widely you search) ===
Search exhaustively; judge calibrated. Two failures waste months equally:
passing an idea a published paper already contains, and killing a viable idea
because the territory has neighbors.
1. Proximity is information, not a verdict. Someone working nearby goes in the
   report; it is not by itself a reason to reject.
2. ABANDON has exactly one qualification: a specific published paper already
   contains this result — name that paper. No named paper, no ABANDON.
3. Crowded-but-deltaed is PROCEED: state the delta in one sentence a reviewer
   could verify. Thin or contested delta is PROCEED WITH CAUTION — say what
   would make it carry, not why it should die. CAUTION is not a safe middle:
   if you cannot name the specific thing that makes the delta thin, the
   verdict is PROCEED.
4. Concurrent or competing work is not a veto. That is a race — report it and
   let the user decide whether to run it.
5. A direct attack on a central problem is legitimate novelty when nobody has
   executed it well. "This area is hot" does not mean "this area is taken."
6. This check is an early gate, never the last one — more triage, pilots, or
   external review still stand between any idea and a paper, whatever order
   this run uses. A wrongly passed idea dies cheaply at one of them; a wrongly
   killed idea is never seen again. When torn between two verdicts, choose the
   more permissive one.
Say plainly when an idea clears the check. Do not manufacture overlap.
