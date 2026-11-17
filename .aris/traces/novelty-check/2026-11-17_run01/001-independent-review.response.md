原文细化：RegionCL Sec3.2 PDF页6–7的MoCo实现是mixed区域p/c与来源图的全局key作正（p/c mask pooling，q/k global avg pooling），不是用户的‘同一几何区域—同一几何区域’；可说来源原则已覆盖，不能说具体正对完全相同。SlotCon Eq6后原文明确 negatives含‘all slots from other images’（PDF页5末–6首），因此共享prototype也没有消除跨图同语义假负；用户若确实按伪类筛掉这些负对，仍有具体差异。UM-SAM的DINO聚类更正已核实。

① 结论：PROCEED WITH CAUTION。可以继续作为扩刊主线；本次核查未找到完整重复方案。薄弱点明确：聚类、来源正对、语义负对分别已有先例，新意须落在“融合后如何构造正确的区域关系”。

② 最接近的先例

- [ALPS](https://arxiv.org/pdf/2406.10855)已包含SAM区域特征、全数据聚类、跨图共享伪类和分割预训练，并有医学验证。这部分不能独立当核心创新。
- [RegionCL](https://arxiv.org/pdf/2111.12309)已按paste/canvas来源构造正负对。不过其MoCo实现将融合区域与来源图全局表示配正；用户的同位置区域对应并非完全相同。
- [ReCo](https://shikun.io/projects/regional-contrast)已有异类语义负样本。[SlotCon](https://proceedings.neurips.cc/paper_files/paper/2022/file/6818dcc65fdf3cbd4b05770fb957803e-Paper-Conference.pdf)已有“同样本、同原型跨增强作正”，但正文明确把其他图像的所有slots作为负样本。
- [UM-SAM](https://papers.miccai.org/miccai-2025/paper/2296_paper.pdf)使用SAM masks＋DINO特征聚类，后续才蒸馏SAM特征，不能写成SAM特征聚类。

③ 能成立的增量

“来源positive／语义negative”这个口号本身不足以构成新意。但有一个可核查的差异：**在跨病例融合中，用实际来源建立局部内容对应，再用共享伪类限制跨病例负对，不把同簇病例直接拉成正对。**它针对RegionCL按图像身份排斥、SlotCon跨图全负的问题，具备明确的问题导向。当前还不能把这一效果写成已经成立。

④ 最严重的推论

95.7% purity不能推出“异簇就是异器官”：一个器官拆成两个完全纯净的簇，purity仍可100%，两簇却会被误推远。这直接关系到核心负样本是否正确，比“是否用了新模块”更关键。

另外，B同位置不要求属于k，所以不能称“同语义组织替换”。C若监督原图A标签，应称原图语义恢复；若监督可见融合内容，标签应随实际来源组合。重建A与区域对比并存不自动矛盾，但两者的学习目标须讲清。

⑤ 建议表述

问题：跨病例区域融合后，内容来源与组织类别并不等价，如何同时保持局部内容对应和合理的跨病例区分？

Insight：用可追溯的来源确定正对，用跨病例伪语义约束负对，让两类信息各自承担适合的监督任务。
