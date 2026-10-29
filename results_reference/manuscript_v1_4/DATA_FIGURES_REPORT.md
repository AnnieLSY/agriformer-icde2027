# 数据图表交付与逐格溯源报告

交付核验时间：2026-10-28 20:02 JST。这是制作与审计记录；图表及图注为论文草稿素材。

## 1. 交付状态

已生成 Table I–V 的独立 booktabs LaTeX 文件、Fig. 3–5 的矢量 PDF 与 300 dpi PNG，以及每项独立的直接读源脚本。所有交付文件位于本目录。未训练模型、未重算实验、未修改已有正式结果或 Fig. 1/2。任务书允许的缺失值已明确标为 — / not recorded；可用数据范围之外的数值没有补造。

**重要限制**：Perm 没有可用的配对均值/成立数；AUS 推理时间未记录。不能从臂中位数恢复配对均值，也不能估算缺失时长。

| 交付文件 | 字节数 | SHA-256 |
| --- | --- | --- |
| table_i_related_work.tex | 2020 | ac5735ddc9ef17b5ff29a127851b7251a0347d61fe3778921fd92bea44d39df7 |
| table_ii_data_profiles.tex | 1538 | a803bdb56b6b03a3afe9b433c947a7378364c4625188a3a0df6e4dbc64ed4e77 |
| table_iii_holdout_comparison.tex | 2857 | 75cc1a14ece080f95515999393f2db0c5684117d7fa52d48c3168a7229e256ac |
| table_iv_replacements.tex | 1674 | d548b6e7e601fde65bd973ce0d8bc6e3539d3177d0d4b673b4610a3a20e5df45 |
| table_v_efficiency_parameters.tex | 1479 | e35d2a7048bc9da07865710a20c42727825b07159f12c978f0085ecd9e7b69bd |
| fig3_tas_gain_decomposition.pdf | 58707 | 09e75b93def84fb616b68a15c46d95f9ba99f4d499715aacbf7d20b315b2e13f |
| fig4_data_conditions.pdf | 67278 | 0a0c7e62f7088fd4df2727ea5ee1e2aedbc124398c13e9a797519d23612a3374 |
| fig5_preparation_validity.pdf | 57866 | 0c3877b77d170c9cd262f1494506f79db9bd5f251f632e9babed212fe30a0e94 |
| fig3_tas_gain_decomposition.png | 61283 | 5901f199e5949efe43e4423a3f7637cfd2b547ccfe4893440190bfc594fa8bc8 |
| fig4_data_conditions.png | 236394 | 556d85e666dcf86361073fee74a09211598f12bb905d6e84366f2a86cfae6897 |
| fig5_preparation_validity.png | 148386 | e60b84fa54b7a6f806cdf081dac156912d4503cdc7f9015084d02915f8f729ce |
| fig3_caption.tex | 613 | 9659618e521ae75a86d7456f939879eff876282db6e7982c334a656e809010bd |
| fig4_caption.tex | 796 | 889cd85265294c414d6e06804ee9a1f9a1428315f9cb6ec4e8a239c434a73bb8 |
| fig5_caption.tex | 635 | a4509ae4ade6ccc74a27f5c692b23937b36d1368a89a8aac486830938599f68e |

额外提供 `table_preview/main.pdf`（IEEEtran 实编译五页预览）、图注 `.tex`、`*_source_data.csv`、`*_evidence.json`、`*_provenance.csv`、`qa/VALIDATION.json`、字体检查和渲染截图。`previous_build/` 仅存放进入本轮前已有版本，不能用于最终稿。

## 2. 执行约束与 Skills

先读框架与完整实验账本，再依次读取 v2 `_shared/references/governance.md`、`routers/route-scientific-artifacts/SKILL.md`、`modules/create-related-work-tables/SKILL.md` 及其 `references/table-patterns.md`。另读取 governance 要求的术语、主语、词汇发明、术语证据和逻辑连续性检查文件。Table II–V 和 Fig. 3–5 按任务书统一样式；PDF 检查使用 pdf skill。没有加载 agents/openai.yaml，没有启动子代理。

`ICDE_manuscript/.codex/manuscript-profile.yml` 已按用户确认的证据口径更新。任务书 §1.3 的数据集/比较取舍覆盖 governance 的基线条款。数据集严格为 AUS2015、GABI、Ward、lentil、pine、rice、wheatG；未加入独立的交叉验证跨模型性能表或 EasyGeSe 跨模型排名。Fig. 4(d) 和 Fig. 5 保留任务明确指定的描述性散点与审计计数。

## 3. 图表口径

| 图表 | 口径 |
| --- | --- |
| Table I | 23 篇固定文献样本；17 篇单目标、5 篇联合目标、1 篇测试端辅助输入；VMGP 独立核查，不并入 23 的分母。AF 的 1/1 指本研究一个设计，不是文献发生率。 |
| Table II | 7 个数据集；性状数包含目标性状；缺失率乘 100；SD ratio 与 C_b 分列。小麦 GBLUP 15 个外层单元，其他数据集按源文件定义。 |
| Table III | 固定留出；仅保留在 AUS2015、GABI 和 Ward 三个群体上都有结果的 13 个模型，加 AF 共 14 个条目。每个数据集×指标独立取该模型最优已记录配置，排名仅在 14 个展示条目中重算。另有 30 个仅在 AUS2015 评估的回归器未列入，完整结果位于 HOLDOUT_FULL_PANEL.csv。 |
| Table IV | 先取各数据集已记录的配对均值，再对数据集等权平均；成立数逐数据集读取预登记结论，FG1 用预登记的均值≥0.01 且正向折比例≥60% 规则。AUS 的 SBV 与事后校准按指定折内敏感性版本；w/o TAS 按明确指定的 strict FG1 行。 |
| Fig. 3 | 两组柱分别是平均 Δln PCC 与平均 Δln C_b；它们相加得到平均 Δln CCC，而非原始尺度 ΔCCC。保留任务指定 E2 的原存储协议，不混入 FG1 的严格重跑数值。 |
| Fig. 4(a,b) | 每个比例保留 AF 及排名最高的两个对照；对照身份直接呈现在图例，未进入前二的位置不绘点。BayesB 使用修正后的专用字段；其他对照直接读取 full_ranking 中保存的精度。 |
| Fig. 4(c) | 仅绘源中真实存在的 0/10/50%；对保存的遮蔽种子/模型种子记录等权求均值。AUS AF 的 delta 字段为空，使用同一 mask_seed 的 0% CCC 减该比例 CCC；没有补零。其他文件直接读取已记录的下降量。 |
| Fig. 4(d) | R6 中 included_in_n7_without_bean=True 且 comparator=GBLUP 的 7 行；Spearman 由保存的两个坐标向量的秩相关得到。只作描述，不画回归线、不报 p 值。 |
| Fig. 5 | FG2 规范 CCC 加已记录 inflation 得天真 CCC；与修正后的逐数据集决策文件互验。难度排序取 wheat3/AF/CCC；虚假领先计数取 R3 的排除版本，并与经典对照审计的逐数据集布尔值互验。 |
| Table V | 从身份审计 §3.5 解析原始标记数和逐折维度，不硬编码结果。准备占比仅使用 lentil、pine、rice 和 wheatG 的 80 个正式 AF-MT/AF-ST 单元，逐单元计算 preparation/total 后取中位数。AF 训练时间另自 R5 strict_AF_CV/AUS2015/AF-MT。学习率范围是四个数据集的内层选模 PCC 范围。 |

成立规则参考 `pilot_20261013/final_gaps_20261026/PROTOCOL.md` §FG-1 与 `context_learner_generality_20261026/PROTOCOL.md`（均值至少 0.01，正向比例至少 60%）；规则文件只用于解释判据，不引入额外实验数值。其余成立标志直接读取各指定结果文件。

### Table IV 最终单元格

| replacement | learner | mean_delta_ccc | established | datasets |
| --- | --- | --- | --- | --- |
| w/o SBV | MLP-Dual | 0.021830490122449 | 3 | 7 |
| w/o SBV | Ridge | 0.0020433826936848 | 0 | 7 |
| w/o SBV | AF | 0.3364128808693633 | 7 | 7 |
| SBV to PCA | MLP-Dual | 0.01351799270107 | 4 | 7 |
| SBV to PCA | Ridge | 0.0020355337591458 | 0 | 7 |
| SBV to PCA | AF | 0.110067402801024 | 7 | 7 |
| w/o TAS | AF | 0.1022528346054535 | 7 | 7 |
| TAS to linear | AF | 0.0970638263764522 | 2 | 3 |
| w/o TAS | MLP-Dual | -0.0109934764527507 | 0 | 3 |
| TAS to Perm | AF | 0.0208711925694597 | not paired | 3 |

## 4. 缺失项与使用边界

| 位置 | 缺失项 | 处理 |
| --- | --- | --- |
| Table I：推理输入 | 单目标 17 篇和联合目标 5 篇的逐篇推理输入字段 | 结构化文献文件没有单独编码该字段，表中为 —；不从训练目标推断推理条件。VMGP 使用官方代码证据。 |
| Table IV：Perm | 配对均值及逐数据集预登记决策 | E1a 仅记录各臂中位数/极值/种子数，因此均值与成立数为 —。中位数差保留在审计证据中，不代替配对均值；不把账本 N20 的 2/3 当成 E1a 中的决策字段。 |
| Table IV：校准与学习器 | 四个 EasyGeSe 数据集的事后校准；Ridge 的 TAS；MLP 的校准/Perm | O_SUMMARY 的 C 键只提供 MT 对 ST，未提供事后校准。校准行分母为 3；其他未记录格为 —。 |
| Fig. 4(b) | 100% 标记比例 | 保留空位置并标明 not recorded；不将 100% 训练样本实验冒充 100% 标记实验。 |
| Table V | AUS 完整准备耗时、推理耗时 | R5 对 total preparation 与 inference 记“无记录”；不从 BayesB 单项时间估算。EasyGeSe 准备占比独立由四个保留数据集的 80 个单元计算。 |

## 5. 与框架及历史记录的逐项核对

| 框架位置 | 源文件结果 | 结论 |
| --- | --- | --- |
| §5 RQ1：AUS 居中 | 在 13 个三群体共同模型加 AF 的 14 个条目中，AF 排名为 AUS2015 6/8、GABI 4/2、Ward 9/1（PCC/CCC）。 | 排名只对三群体的可比模型计算；30 个 AUS2015-only 回归器未混入其中。 |
| §5 RQ1：种子均值 | AF 主数值是种子平均预测向量上的指标；逐种子指标均值±样本标准差另行报告。 | 两种统计量保持分离，种子数为 AUS2015 20、GABI 5、Ward 5。 |
| §5 RQ2：AF 7/7、MLP 4/7、Ridge 0/7 | SBV→PCA 为 7/7、4/7、0/7；w/o SBV 为 7/7、3/7、0/7。 | 两个替换实验必须分别叙述。 |
| §5 RQ2：事后校准 GABI +0.126、Ward +0.149 | GABI 0.126472958、Ward 0.149254170；AUS 折内版 0.015464351，未通过成立规则。 | 前两项与框架一致；三群体成立数是 2/3，不能扩写为 3/3。 |
| §5 RQ2：TAS 严格 CV 与尺度分解 | Table IV 使用指定 strict FG1 + O；Fig. 3 的 E2 使用历史 K + O。GABI 的原始 ΔCCC 在两个版本分别约 0.131 和 0.265。 | 协议不同，不应将 Fig. 3 的数值称为 FG1 strict 的增益分解。按任务保留指定源，未换用未授权结果。 |
| §5 RQ3：样本 4 个比例、标记 3 个比例均第一 | FP1 的全部 7 个比例中 AF_rank_of_8=1；标记优势 0.049779–0.085497。 | “标记领先 0.050–0.130”上限不符；0.130367 是训练样本 25% 的优势。 |
| §5 RQ3：测试端缺失 AF −0.003，GBLUP −0.234 | AUS 50% 遮蔽的平均下降：AF 0.003399727、GBLUP 0.234374381。 | 三位小数与框架一致；GABI/Ward 没有 50% 记录。旧图把 AUS AF 空 delta 字段填 0 的错误已修正。 |
| §5 RQ3：7 数据集 ρ≈−0.68 | Spearman ρ=-0.678571429，n=7。 | 一致；标记 descriptive。 |
| §5 RQ4：28/28、τ=−1、CCC 6/7、PCC 7/7 | 七数据集×两个学习器×两个指标的修正 FG2 原规则成立数为 28/28；三个小麦 AF 的 CCC 顺序全反转；虚假领先 CCC 6/7、PCC 7/7。 | 一致。28/28 是所选七数据集的计数，不使用包含被排除数据集的总数。 |
| §5 RQ5：压缩 24–35 倍，准备占比 3.68% | 按逐折正式维度，压缩约 23.733–35.003 倍；四个保留 EasyGeSe 数据集的 80 个单元中，逐单元准备/总耗时比的中位数为 3.675607440%。 | 表中显示 3.68%，分母为 80；准备时间和总耗时另报各自中位数。 |
| §5 RQ5：学习率变化 0.004–0.015 | 四个保留数据集范围 0.004089031–0.014639333。 | 三位小数一致，但只能称内层选模 PCC 跨档均值范围，不能称外层测试敏感性。 |
| 账本 PF-E5 与 Table II 指定画像文件 | PF-E5 记 wheatG 为整数 −2/0/2；DATA_PROFILE.csv 的 genotype_encoding 记包含非整数 SVD 插补值。 | 存在正式文件间的编码描述冲突。本任务按指定 DATA_PROFILE 原样作表，未修改结果；需在源文件维护阶段解决。 |

## 6. 自检结果

- 逐格证据：**1135 条全部通过**。验证器重新打开原始 CSV/JSON/Markdown，按行/列、JSON 键或表格正则读取值，并重新执行只读汇总算式；检查不是仅确认路径存在。
- 输入保护：**35 个受保护文件 SHA-256 一致**，包括 Fig. 1/2；账本追加为任务书 §5 明确授权的唯一目录外写入。
- 数据范围：所有源数据导出中的 dataset 值均属于指定七数据集；图表文本无被排除数据集，无工具/AI 制作说明。未输入缺失值为 0，未插值。
- 三张图：PDF 页数各 1；宽度精确为 3.5 / 7.16 / 7.16 英寸；PNG 为 300 dpi；可见标签的设定字号均为 8 pt；PDF 字体嵌入并子集化。正文 Times New Roman，数学符号为 STIX。
- 五张表：使用 IEEEtran conference 类和 booktabs/tabularx 实际编译成功；最终日志无 Overfull/Underfull、未定义引用或 LaTeX error。Times 系 Nimbus Roman 文本已嵌入。逐页查看了最终 PDF 渲染，数字、配置名、表注没有遮挡或截断。
- Figure PDFs 已逐一渲染并检查，图例、数据标签、轴标题和面板标题可读；颜色之外同时使用符号、线型或纹理。
- 原有记录称缺少编译器；本轮找到已有 Tectonic 0.16.9。IEEEtran 依赖下载曾重试，最终编译成功；此为已解决的工具问题。
- 图表所列值统一按要求显示三位小数或计数整数，溯源记录保留源精度。坐标刻度、设计比例和图表编号属于排版或任务规格，不伪装成测量结果。

### 术语与主语检查

| 术语 | 类型 | 定义/来源 | 处理 |
| --- | --- | --- | --- |
| SBV / EMV / TAS | O1：已由框架批准的研究定义 | Scoped Background View / Effect-Ordered Marker View / Train-Only Auxiliary Supervision；框架 §2、Fig. 2 | 统一使用批准名称；删除旧图表中 supervised background view、trait-assisted supervision 的错误展开。 |
| PCC / CCC / C_b / SD ratio | 按指定指标定义使用 | PCC=Pearson correlation；CCC=concordance correlation；C_b=CCC/PCC；SD ratio=SD(prediction)/SD(observation) | 保留既有指标名，不新增术语流行性主张；SD ratio 与 C_b 不合并为一个量。 |
| ΔCCC / Δln CCC | O1：本图表的运算定义 | 完整模型减替换模型；对数差仅用于 Fig. 3 的加法恒等式 | 明确原尺度与对数尺度；不声称两个对数项能相加得到原尺度差。 |
| scoped / naive / false lead | R1：实验条件与描述性结果 | 训练划分内准备；拆分前准备；天真流程制造相对于对齐经典对照的表面领先 | 图注明确操作和计数；没有新造缩略词。 |
| AF、VMGP、MLP-Dual、GBLUP 等 | 源文件中的正式名称 | 任务书、固定面板、文献审计；VMGP DOI 链接 | 保持原名；表 I 没有首次/全称否定；未把代码核查写成论文全文核查。 |

表注使用明确的“bars/values/each cell”等主语说明所画量和算式；没有让图表承担研究者的推断行为。统计限定语与对应结果置于同一表注或图注；不把生产流程说明混入论文图表。

## 7. 正式输入索引

| ID | 正式源文件（绝对路径） | SHA-256 |
| --- | --- | --- |
| S01 | ${WORKSPACE}/CLEANUP_AUDIT_20261022/DUAL_INPUT_IDENTITY_AUDIT_20261025.md | 5bf76399e120f3b95b0b2626c32bc5c86f02a610b5f0f5f229c6bb3db08342df |
| S02 | ${WORKSPACE}/CLEANUP_AUDIT_20261022/READONLY_RANK_REVERSAL_CLASSIC_DATASETS_20261025.csv | f1b446e15afd6b3417da1215ce4d88c3d182a13df51f02412fe710ad82d9aa20 |
| S03 | ${WORKSPACE}/CLEANUP_AUDIT_20261022/READONLY_RANK_REVERSAL_RANKS_20261025.csv | 35b6183703c2aa13e3457dd90c7c7b384fb97e16f8a79b33b4fcb43f03956bca |
| S04 | ${WORKSPACE}/ICDE_drafts/ICDE_story_v7_framework_v1_1_20261028.md | 7c6c9ec21e64337bbea035bcf5e8de74a62e8e6061ef91af9ac9f599aad494a9 |
| S05 | ${WORKSPACE}/ICDE_drafts/LIT_ASSUMPTIONS_20261026.csv | b63b79b8f03d5b306bc1c809aade133ced9d329bf16025ed9e2ac7bfc4f0175c |
| S06 | ${WORKSPACE}/ICDE_drafts/VMGP_AND_CITES_20261028.md | a1af3b60624c27e8d01b5908367de1a02a781e4dc89f61d215a1bfe69a6db4cc |
| S07 | ${WORKSPACE}/pilot_20261013/aus_infold_pheno_sensitivity_20261025/SUMMARY.json | 53813c8e9638f3449ead7234dded46769a7ded97abfbc59e2e439d60b2a6a1d9 |
| S08 | ${WORKSPACE}/pilot_20261013/context_learner_generality_20261026/SUMMARY.csv | 33fe4f33860c4bbd38870be1b258063622373f015ff2e2b55e91534f7ab35862 |
| S09 | ${WORKSPACE}/pilot_20261013/data_profile_20261026/DATA_PROFILE.csv | 4c7df77f60b9ebe632f8916e1509ef76378443b2eec512dbc31f0fd02877c92e |
| S10 | ${WORKSPACE}/pilot_20261013/final_gaps_20261026/FG1/FG1_OLD_VS_STRICT.csv | 080f1c2c5638eab94a921995316c4ae2c29402061dc19815cbd2256991989f67 |
| S11 | ${WORKSPACE}/pilot_20261013/final_gaps_20261026/FG2/FG2_D_DECISIONS.csv | 0bb6d27f042b51e49782a08234aa30bf1922db39cbbaf5f54d6ae4c46e84d286 |
| S12 | ${WORKSPACE}/pilot_20261013/final_gaps_20261026/FG2/FG2_SUMMARY.json | ba7d97260369739181360f69cb32e9c6fdfb41a0cf476b0d31d12bd328db9c38 |
| S13 | ${WORKSPACE}/pilot_20261013/final_pack_20261027/fp1/FP1_RATIO_COMPARISON.csv | 60d8e64b3b332b050976f77aaafa8dd0eee5003d04827e1864c6e74dd4b51faf |
| S14 | ${WORKSPACE}/pilot_20261013/final_pack_20261027/fp3/FP3_E8B_LR_RANGE.csv | 30fe924c7482dbd8de64b3bcfbfe78baa8caf61cfefb87b0973e88cb83c48ae1 |
| S15 | ${WORKSPACE}/pilot_20261013/holdout_fill_20261027/HOLDOUT_FULL_PANEL.csv | df40e072eff1e389d7889370bdb1f2f4e7e024d711939ec072af92124e5cd3a9 |
| S16 | ${WORKSPACE}/pilot_20261013/icde_readonly_pack_20261026/R2_AF_SEED_SUMMARY.csv | 150dac007fad1422f6ed276234fea4849c3348667b942f34cdea7ece4e87f811 |
| S17 | ${WORKSPACE}/pilot_20261013/icde_readonly_pack_20261026/R3_WITH_WITHOUT_BEAN_COUNTS.csv | 9adfe7f5a61c2e60a254cf97dd06b4b0e9d44ccf46f84ee481a40e00ac7e835d |
| S18 | ${WORKSPACE}/pilot_20261013/icde_readonly_pack_20261026/R5_RECORDED_TIMINGS.csv | 475a0baa9ab4d733d2ea7ddacfb95bae7504c4fdcdd70e25b56b41b5e143da9b |
| S19 | ${WORKSPACE}/pilot_20261013/icde_readonly_pack_20261026/R6_APPLICABILITY.csv | 6a9ba18ddf3ee993e04842573cf3011662918f49ae1f456018e86ced03f41d22 |
| S20 | ${WORKSPACE}/pilot_20261013/packaging_followups_20261025/E1/E1a_S_seed_metrics.csv | a21de67e18b255e0d3f5018c47c2028cec2d071af77a4ed674f0092b581752c2 |
| S21 | ${WORKSPACE}/pilot_20261013/packaging_followups_20261025/E1/E1a_S_summary.csv | 80da954829c6032e2fdf6d2f42351592b5ae89b590e00a49ba5683eb0d04036a |
| S22 | ${WORKSPACE}/pilot_20261013/packaging_followups_20261025/E2/E2a_dataset_summary.csv | 256203d1c51b4cbfd1085703f367199bde3d3f00e0d026a4b9555423e1ec871a |
| S23 | ${WORKSPACE}/pilot_20261013/packaging_followups_20261025/E4/E4_DATASET_DECISIONS.csv | fdc0b84095f8ea5e01e9885355335fef183329a42ca3c3e43ccce638fd1d3ad6 |
| S24 | ${WORKSPACE}/pilot_20261013/run_v13/A_GBLUP_missing.csv | aa3745da1caa6f436f5883cdb5abb95e1422b2ab47860386971b9f62deac88ae |
| S25 | ${WORKSPACE}/pilot_20261013/run_v13/A_X4_missing.csv | c98716b2f98a1e020d6f2dfd7dd7f4fea7b1d1c41e6f6201ff9ae644a8be45cf |
| S26 | ${WORKSPACE}/pilot_20261013/run_v13/E_GBLUP_missing_external.csv | 778ececed77274ce38c14061c81c5c747092f89f5021fa83376b43297c91ecea |
| S27 | ${WORKSPACE}/pilot_20261013/run_v13/E_X4_missing_external.csv | 5efb4a222943b0bcbae133cc361769615602e53284f3cfc31fdd689a989b0e55 |
| S28 | ${WORKSPACE}/pilot_20261013/run_v13/K/K_SUMMARY.json | 23f991e3764df3d80746b889acf52d4451ac9265588e607d26fc683b27ca0937 |
| S29 | ${WORKSPACE}/pilot_20261013/run_v13/M/M_SUMMARY.json | 65ff588358016da1359f54bb054237310e47c02df674c49dc93df7d61642829a |
| S30 | ${WORKSPACE}/pilot_20261013/run_v13/O/O_SUMMARY.json | fb22feabb74decca964e41d50b87928f3fc0cb65f1c12a1038901fae00b85657 |
| S31 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f1_AF-MT.json | f75404eadeeaf00c05684f9424c376dcc7b667514eced9565f120cfedae173b8 |
| S32 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f1_AF-ST.json | 3edd7f80e82de3856b57b9c480b1c1b31f2222747de7e467a200a2df904a1689 |
| S33 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f2_AF-MT.json | e3832010e86e3711f01c01dc57d21c6faf97feff0670240d7f90642aa183e1cb |
| S34 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f2_AF-ST.json | c767e2c362b2d3d51981641557f70faf49713ea714ff4fca09e8e5d401e372b4 |
| S35 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f3_AF-MT.json | 9f639b084e6ed1d8ab51c6e843507039b79ce473b71bc5df2e81f760f289bf69 |
| S36 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f3_AF-ST.json | d18d0c58a9904505335f0304d53204e09a2533e9e3effe9ef1e3fd7c7cc28cb6 |
| S37 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f4_AF-MT.json | 4be649edc1ea80bb96f8f26c312296356fa4310f6596ab33cf154e80b73ae3aa |
| S38 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f4_AF-ST.json | fd7674bcbed20f957f1420344b7f2ba95e485a3b0bbf46c88f8085d2f47aea0c |
| S39 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f5_AF-MT.json | a34ea43f35718175c1f7295e9d2fda3ddc7529881c39532d3f8828e1d78f4417 |
| S40 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r1_f5_AF-ST.json | afabd60913cfa333b5e573be7831c253f65b025886dc746b0cc0d517b097d7c7 |
| S41 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f1_AF-MT.json | 27d133c3eb9bc9b777c161b1cc590957521733688ef1da11415e1f93f0f6de6d |
| S42 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f1_AF-ST.json | 5bfe7f1697ac8247d2ad3012100ad1a0bbe98bef14b19aef0ccd5a92376a6f39 |
| S43 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f2_AF-MT.json | 2a330e514599f81239438b8dc92ded2ca784e7b9cd5c817df3a5c706b41cbd42 |
| S44 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f2_AF-ST.json | 259fda37720005c895fb3af561402bbfa0c1e713de4779cab88695499e99e3b5 |
| S45 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f3_AF-MT.json | d720f25eb1d4ce4e66c01fca8f008f68138a71244ee9c7321e097113d96fb768 |
| S46 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f3_AF-ST.json | c526323ce12b2c3b4a5c207cb152b8889c0cc9cd77d4856b9d2e94f7a9c5019f |
| S47 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f4_AF-MT.json | 0fb991de5d856dd0d8e6e7c390510d57b6d11f0b5b794231f3cd737aaea7ee76 |
| S48 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f4_AF-ST.json | 5940778956efec923e13ea8e95ce270e7fe01e550c9199f664b5d0717713c911 |
| S49 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f5_AF-MT.json | e45c86a32605847162eb6cb588a88f8489c91d93db628e241e226374d7e162ba |
| S50 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/lentil_r2_f5_AF-ST.json | 8dcb024a2bd43029e3e286a71fa0593908d61b70a0109a923aeb14962643ccaa |
| S51 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f1_AF-MT.json | 47737d2a2b08c10221aa4019af07ef0a6e3fb35ab4ada249eade04cdd2edf04e |
| S52 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f1_AF-ST.json | a0baf80e032c7b64e36cfee285b10d81dd4317e085c0683bf7cc0926df968273 |
| S53 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f2_AF-MT.json | 5eaefb94337bd8fa1c4f87b33c61dbbbdd4d4684a646f96a183c7ce3673228f1 |
| S54 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f2_AF-ST.json | 770a5ba35818dc3b8639a6914b1613344e0d584d60480e9d2fa4a14ed6e01fd3 |
| S55 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f3_AF-MT.json | 57bf4aa816bad2eec430512762ba2686e27a192ce17c3aafddf804fe82d39bcb |
| S56 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f3_AF-ST.json | 51d6b030f9f16e5b5753053ed7d7be118321384c9778ef153097a40911b4e721 |
| S57 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f4_AF-MT.json | 58ca4249605d2f6078f2586d3d62d8eabee64a85fcae9d456f37f2f35c87f234 |
| S58 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f4_AF-ST.json | d03709ce182fd80bef3d2acd7e8c7808cc03a066a832336a9cf9fadb3be83b79 |
| S59 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f5_AF-MT.json | 841df190a202b0ea1c21a1f5787baf81b7be7a47102b7662d30101e11df72ca5 |
| S60 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r1_f5_AF-ST.json | 77681c25574017fb4e006703a523dd47b14b988ee89511aebff04175b88e8a6e |
| S61 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f1_AF-MT.json | 60e98576ea0b8d6c23f1fdd56abe8eb9549878f598d29d14b86854083974252d |
| S62 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f1_AF-ST.json | abfd54586864e4659f8960b373ff7e3df6af88977b7832b4382ad55e2a62d51a |
| S63 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f2_AF-MT.json | 9a828731c0d015176e19bf40f8a10711cb9593b7604c4a99e83b7e2bca300683 |
| S64 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f2_AF-ST.json | 9efdaaac27da2b75b769d0fd956c43c2469b12a49f492c5c020c06b82f699842 |
| S65 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f3_AF-MT.json | c137488e7807e9b1d9149f4c2413f766e16808238f5beada58627cbf84e72fc8 |
| S66 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f3_AF-ST.json | 31382d5d81cc4afc7a2a09ddb0e025aa601d8041343c75b76c0dfd9b40f02059 |
| S67 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f4_AF-MT.json | b273711b1af49d756a182e824d3a7d2e013f15eba06edd43dc7361c549a71348 |
| S68 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f4_AF-ST.json | 84451637d59ce17590b7a63473b8dbad7ea5e83d40a287ce24620d9793eefcfd |
| S69 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f5_AF-MT.json | 4d17ab2f1a339e50beffd0ea2dbbc1dd0f1bca4ed0dcaf9f435a9e0c071d368c |
| S70 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/pine_r2_f5_AF-ST.json | e93cc0da9fa8fa9d31064240d396e36b1e5929fcda028ba06d0b640cca0b9253 |
| S71 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f1_AF-MT.json | fef290ccabc94e13bec63846b9ad2c844ed10310f16cac825eebeb54d91c7000 |
| S72 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f1_AF-ST.json | 55e41332deef6afa2eed1d6ffc404333c7a4c006d446e2c2fe2f3f9ef2d318c9 |
| S73 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f2_AF-MT.json | 5764932fe1ef649940396d263835a5fe5d5eca7cb32abbf450d63ad74b818ab9 |
| S74 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f2_AF-ST.json | 354b7232d459b1ef32b37f0568af824460fabaa931972460f06c9c045f1b8d29 |
| S75 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f3_AF-MT.json | c9546beef7039d1b7029bf6491476f5e88acaf5a548f675543788641e3a35fd3 |
| S76 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f3_AF-ST.json | 1df1983b81941e7706ee4a59750a2a53c048ecaaf722e3022f711755ec9102c8 |
| S77 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f4_AF-MT.json | 3870ffef3661bae7f7518dad31edadec52593808d963ee2bdcfdb2bb04b3b19d |
| S78 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f4_AF-ST.json | a8db578cd813eba837a1f319d272ad2227363eb53a5dc325fa9256b0906d94e7 |
| S79 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f5_AF-MT.json | cabc1db707544c73e06316352d7e9c53819e382d7fb7d5b7814e07df3e03535c |
| S80 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r1_f5_AF-ST.json | 5fa0cdea969eba6ea3fe879936bec89769a65a580c1a1a6aeda16247b7b5570d |
| S81 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f1_AF-MT.json | dda6c9205e5e80a9a4a38f65013684dbf880545930ab4c05623ae878391c79a9 |
| S82 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f1_AF-ST.json | 516a2896f4c8e9fab064a39940981e946d1a443cb39973cac94b3579a3e55805 |
| S83 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f2_AF-MT.json | a5ef14feb77a49784e6429b007ab763fef060e76e57729d678c7544cadf4a138 |
| S84 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f2_AF-ST.json | 9d8619434580c77e06bce693a1a3f5d36c3fb2c0ae06cea689a34ea027cd3d6d |
| S85 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f3_AF-MT.json | 1bbd2d9a4e0628e348a1d3200b2416458e7e103b6e2c0f4570768f3aa52fcab9 |
| S86 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f3_AF-ST.json | 1431e7af9f8145bc2998ea524634d16c5aeb01f537d4e0d279616dedcfcf857f |
| S87 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f4_AF-MT.json | 46302fab5dfcecaf4f07fa5bfe809deda70db95e52d41763241dcbd5125ed375 |
| S88 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f4_AF-ST.json | 9f088d146c6bc3a7ccf677889f99384799d4129728641cb8e87b1893825a4d24 |
| S89 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f5_AF-MT.json | a14512fb3e59cbb1ab71c632dbd01c79a0c177c0431e4603a1c4d81196c6915e |
| S90 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/rice_r2_f5_AF-ST.json | 975bad76ed7f2c9ea941e9a9ad2f3f61ddcc005f52f0e501b4a4a2b6a9ded6a3 |
| S91 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f1_AF-MT.json | ce36bc4b6dee1327a5119c18a9405873dc210172b6d4b628ad66cbcc3ed715aa |
| S92 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f1_AF-ST.json | 13778601d61edac710146360e76acaaa8dc90eede960b96c4b2f26bcfa1fb70c |
| S93 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f2_AF-MT.json | d61f1614d0de07cf4537eda7e6641d725a4352f110185d73ebd5115541560956 |
| S94 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f2_AF-ST.json | 952bccba966803f73c34d9d6921d6a1c745393226c8c4119f8cd205c3b516730 |
| S95 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f3_AF-MT.json | 27c0115ad3869b8b12d7c95f5a8ff1c15abb526514d037effcdc920db81169a3 |
| S96 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f3_AF-ST.json | 8c743d4f8fb1703d6d8e0563a1e53a698978715f493b8b025c1258e44ec9b671 |
| S97 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f4_AF-MT.json | 08a749deac9cae2d7034a0af1ec96e4a080f64487c9507d312dfd9448be6612c |
| S98 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f4_AF-ST.json | 959710a4760a95dadce153a7b20dac04dfde630147aa06a696d138709228a613 |
| S99 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f5_AF-MT.json | f1564aa75409d3e9ac77dd775d655c9a58910d1537aa9037674b01120794ec75 |
| S100 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r1_f5_AF-ST.json | 098a44217cd953fe0fa2e155d509b8200ae92213c301c773b02dee196d7f7826 |
| S101 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f1_AF-MT.json | f6d172981273447ba0ed1f7c43868e48c1ec98dfb6f95ca551fc4e80dd4c34cc |
| S102 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f1_AF-ST.json | 725a0fdba4dfcf30cb155d8bf905e6b7698515299be38a023ec8cc812cda064e |
| S103 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f2_AF-MT.json | c6adff40584eb9dfc00c52f16167b20c7faf829596753857daee72b471a3ab41 |
| S104 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f2_AF-ST.json | 59d3c93aca2e2863c07c7ac5c906e1993209cd18415df3b20f09c69054c9517f |
| S105 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f3_AF-MT.json | 26316fd726af6873cec0d11c440f537a3c49547c927d9496ef1f9c849f012aa8 |
| S106 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f3_AF-ST.json | d43afb60c93e213f5c7777465e50de0a42c700babe481a5a74c90e6daf973fdf |
| S107 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f4_AF-MT.json | b668b78968c94a814431d6fa19ea621e066e943cf439629f412d2ae501186deb |
| S108 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f4_AF-ST.json | 27bc30b11295cc9c89157e0a647827ce5fcea41854905b6fb164ec3885d74673 |
| S109 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f5_AF-MT.json | 1329c2952813f4aef1db1f966c21ab0ca778369fdf4fa33e804395a6fde26454 |
| S110 | ${WORKSPACE}/pilot_20261013/run_v13/O/rows/wheatG_r2_f5_AF-ST.json | ede14f698432f8d145986e73bab6335c22dc3f648ac7358b0181e381243c0a02 |

## 8. 逐格、逐点、聚合输入的完整溯源

CSV 行号表示去掉标题后的逻辑数据记录序号（不是在含换行引号字段时的文本物理行号）。JSON 用完整键数组定位。derived 项引用同一图表此前列出的 element，依赖图最终回到正式输入；`*_evidence.json` 保存每个原始输入和算式的机器可读版本。显示值的舍入仅发生在排版阶段。

### Table I

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| studies_examined | 23 | S05: data row 1 / key ; S05: data row 2 / key ; S05: data row 3 / key ; S05: data row 4 / key ; S05: data row 5 / key ; S05: data row 6 / key ; S05: data row 7 / key ; S05: data row 8 / key ; S05: data row 9 / key ; S05: data row 10 / key ; S05: data row 11 / key ; S05: data row 12 / key ; S05: data row 13 / key ; S05: data row 14 / key ; S05: data row 15 / key ; S05: data row 16 / key ; S05: data row 17 / key ; S05: data row 18 / key ; S05: data row 19 / key ; S05: data row 20 / key ; S05: data row 21 / key ; S05: data row 22 / key ; S05: data row 23 / key | count |
| single_target_studies | 17 | S05: data row 1 / key ; S05: data row 2 / key ; S05: data row 3 / key ; S05: data row 4 / key ; S05: data row 5 / key ; S05: data row 7 / key ; S05: data row 8 / key ; S05: data row 9 / key ; S05: data row 10 / key ; S05: data row 12 / key ; S05: data row 15 / key ; S05: data row 16 / key ; S05: data row 17 / key ; S05: data row 19 / key ; S05: data row 21 / key ; S05: data row 22 / key ; S05: data row 23 / key | count |
| joint_studies | 5 | S05: data row 6 / key ; S05: data row 13 / key ; S05: data row 14 / key ; S05: data row 18 / key ; S05: data row 20 / key | count |
| year_min | 2019 | S05: data row 1 / year ; S05: data row 2 / year ; S05: data row 3 / year ; S05: data row 4 / year ; S05: data row 5 / year ; S05: data row 6 / year ; S05: data row 7 / year ; S05: data row 8 / year ; S05: data row 9 / year ; S05: data row 10 / year ; S05: data row 11 / year ; S05: data row 12 / year ; S05: data row 13 / year ; S05: data row 14 / year ; S05: data row 15 / year ; S05: data row 16 / year ; S05: data row 17 / year ; S05: data row 18 / year ; S05: data row 19 / year ; S05: data row 20 / year ; S05: data row 21 / year ; S05: data row 22 / year ; S05: data row 23 / year | min |
| year_max | 2026 | S05: data row 1 / year ; S05: data row 2 / year ; S05: data row 3 / year ; S05: data row 4 / year ; S05: data row 5 / year ; S05: data row 6 / year ; S05: data row 7 / year ; S05: data row 8 / year ; S05: data row 9 / year ; S05: data row 10 / year ; S05: data row 11 / year ; S05: data row 12 / year ; S05: data row 13 / year ; S05: data row 14 / year ; S05: data row 15 / year ; S05: data row 16 / year ; S05: data row 17 / year ; S05: data row 18 / year ; S05: data row 19 / year ; S05: data row 20 / year ; S05: data row 21 / year ; S05: data row 22 / year ; S05: data row 23 / year | max |
| single_preparation | 5 | S05: data row 1 / key ; S05: data row 3 / key ; S05: data row 5 / key ; S05: data row 15 / key ; S05: data row 19 / key | count |
| joint_preparation | 1 | S05: data row 20 / key | count |
| single_train_confined | 2 | S05: data row 1 / preparation_timing ; S05: data row 3 / preparation_timing ; S05: data row 5 / preparation_timing ; S05: data row 15 / preparation_timing ; S05: data row 19 / preparation_timing | count_equal {"target": "train_fold"} |
| single_mixed | 1 | S05: data row 1 / preparation_timing ; S05: data row 3 / preparation_timing ; S05: data row 5 / preparation_timing ; S05: data row 15 / preparation_timing ; S05: data row 19 / preparation_timing | count_equal {"target": "mixed_by_dataset"} |
| single_unclear | 2 | S05: data row 1 / preparation_timing ; S05: data row 3 / preparation_timing ; S05: data row 5 / preparation_timing ; S05: data row 15 / preparation_timing ; S05: data row 19 / preparation_timing | count_equal {"target": "unclear"} |
| joint_unclear | 1 | S05: data row 20 / preparation_timing | count_equal {"target": "unclear"} |
| single_error_scale | 11 | S05: data row 1 / metric_class ; S05: data row 2 / metric_class ; S05: data row 3 / metric_class ; S05: data row 4 / metric_class ; S05: data row 5 / metric_class ; S05: data row 7 / metric_class ; S05: data row 8 / metric_class ; S05: data row 9 / metric_class ; S05: data row 10 / metric_class ; S05: data row 12 / metric_class ; S05: data row 15 / metric_class ; S05: data row 16 / metric_class ; S05: data row 17 / metric_class ; S05: data row 19 / metric_class ; S05: data row 21 / metric_class ; S05: data row 22 / metric_class ; S05: data row 23 / metric_class | count_equal {"target": "correlation_and_scale"} |
| joint_error_scale | 5 | S05: data row 6 / metric_class ; S05: data row 13 / metric_class ; S05: data row 14 / metric_class ; S05: data row 18 / metric_class ; S05: data row 20 / metric_class | count_equal {"target": "correlation_and_scale"} |
| single_correlation_only | 6 | derived:single_target_studies ; derived:single_error_scale | subtract |
| auxiliary_test_input_studies | 1 | S05: data row 11 / key | count |
| VMGP_inference | 官方源码的推理只需要新个体基因型，不需要新个体的辅助性状表型。 | S06: regex (官方源码的推理只需要新个体基因型，不需要新个体的辅助性状表型。) / group 1 | identity |
| VMGP_metrics | 官方评价函数逐性状计算 **MAE** 和 **Pearson correlation coefficient (PCC)** | S06: regex (官方评价函数逐性状计算 \*\*MAE\*\* 和 \*\*Pearson correlation coefficient \(PCC\)\*\*) / group 1 | identity |
| AF_design | Train-Only Auxiliary Supervision (TAS) | S04: regex (Train-Only Auxiliary Supervision \(TAS\)) / group 1 | identity |

### Table II

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| AUS2015:cv_outer_unit_count | 15 | S09: data row 1 / cv_outer_unit_count | identity |
| AUS2015:species | bread wheat (Triticum aestivum) | S09: data row 1 / species | identity |
| AUS2015:n | 494 | S09: data row 1 / n | identity |
| AUS2015:p | 23899 | S09: data row 1 / p | identity |
| AUS2015:p_over_n | 48.378542510121456 | S09: data row 1 / p_over_n | identity |
| AUS2015:genotype_encoding | 0/2 homozygous additive calls; -1 denotes missing | S09: data row 1 / genotype_encoding | identity |
| AUS2015:current_matrix_missing_fraction | 0.0082982483809649 | S09: data row 1 / current_matrix_missing_fraction | identity |
| AUS2015:recorded_trait_count | 9 | S09: data row 1 / recorded_trait_count | identity |
| AUS2015:cv_gblup_prediction_observed_sd_ratio_mean | 0.7694683592323578 | S09: data row 1 / cv_gblup_prediction_observed_sd_ratio_mean | identity |
| AUS2015:cv_gblup_cb_mean | 0.9625807858515576 | S09: data row 1 / cv_gblup_cb_mean | identity |
| AUS2015:missing_percent | 0.82982483809649 | derived:AUS2015:current_matrix_missing_fraction | percent |
| GABI:cv_outer_unit_count | 15 | S09: data row 2 / cv_outer_unit_count | identity |
| GABI:species | bread wheat (Triticum aestivum) | S09: data row 2 / species | identity |
| GABI:n | 371 | S09: data row 2 / n | identity |
| GABI:p | 35143 | S09: data row 2 / p | identity |
| GABI:p_over_n | 94.72506738544476 | S09: data row 2 / p_over_n | identity |
| GABI:genotype_encoding | 0/2 homozygous additive calls; -1 denotes missing | S09: data row 2 / genotype_encoding | identity |
| GABI:current_matrix_missing_fraction | 0.1373948242118666 | S09: data row 2 / current_matrix_missing_fraction | identity |
| GABI:recorded_trait_count | 18 | S09: data row 2 / recorded_trait_count | identity |
| GABI:cv_gblup_prediction_observed_sd_ratio_mean | 0.6546388504190215 | S09: data row 2 / cv_gblup_prediction_observed_sd_ratio_mean | identity |
| GABI:cv_gblup_cb_mean | 0.9090750821214816 | S09: data row 2 / cv_gblup_cb_mean | identity |
| GABI:missing_percent | 13.739482421186661 | derived:GABI:current_matrix_missing_fraction | percent |
| Ward:cv_outer_unit_count | 15 | S09: data row 3 / cv_outer_unit_count | identity |
| Ward:species | bread wheat (Triticum aestivum) | S09: data row 3 / species | identity |
| Ward:n | 314 | S09: data row 3 / n | identity |
| Ward:p | 29949 | S09: data row 3 / p | identity |
| Ward:p_over_n | 95.37898089171976 | S09: data row 3 / p_over_n | identity |
| Ward:genotype_encoding | 0/2 homozygous additive calls; -1 denotes missing | S09: data row 3 / genotype_encoding | identity |
| Ward:current_matrix_missing_fraction | 0.0527888918592605 | S09: data row 3 / current_matrix_missing_fraction | identity |
| Ward:recorded_trait_count | 14 | S09: data row 3 / recorded_trait_count | identity |
| Ward:cv_gblup_prediction_observed_sd_ratio_mean | 0.4139499034060479 | S09: data row 3 / cv_gblup_prediction_observed_sd_ratio_mean | identity |
| Ward:cv_gblup_cb_mean | 0.6842865868332172 | S09: data row 3 / cv_gblup_cb_mean | identity |
| Ward:missing_percent | 5.27888918592605 | derived:Ward:current_matrix_missing_fraction | percent |
| lentil:cv_outer_unit_count | 10 | S09: data row 4 / cv_outer_unit_count | identity |
| lentil:species | lentil (Lens culinaris) | S09: data row 4 / species | identity |
| lentil:n | 324 | S09: data row 4 / n | identity |
| lentil:p | 23590 | S09: data row 4 / p | identity |
| lentil:p_over_n | 72.80864197530865 | S09: data row 4 / p_over_n | identity |
| lentil:genotype_encoding | 0/1/2 additive genotype encoding | S09: data row 4 / genotype_encoding | identity |
| lentil:current_matrix_missing_fraction | 0.0 | S09: data row 4 / current_matrix_missing_fraction | identity |
| lentil:recorded_trait_count | 5 | S09: data row 4 / recorded_trait_count | identity |
| lentil:cv_gblup_prediction_observed_sd_ratio_mean | 0.8538875759498399 | S09: data row 4 / cv_gblup_prediction_observed_sd_ratio_mean | identity |
| lentil:cv_gblup_cb_mean | 0.9781753026854572 | S09: data row 4 / cv_gblup_cb_mean | identity |
| lentil:missing_percent | 0.0 | derived:lentil:current_matrix_missing_fraction | percent |
| pine:cv_outer_unit_count | 10 | S09: data row 5 / cv_outer_unit_count | identity |
| pine:species | loblolly pine (Pinus taeda) | S09: data row 5 / species | identity |
| pine:n | 926 | S09: data row 5 / n | identity |
| pine:p | 4782 | S09: data row 5 / p | identity |
| pine:p_over_n | 5.16414686825054 | S09: data row 5 / p_over_n | identity |
| pine:genotype_encoding | 0/1/2 additive genotype encoding | S09: data row 5 / genotype_encoding | identity |
| pine:current_matrix_missing_fraction | 0.0 | S09: data row 5 / current_matrix_missing_fraction | identity |
| pine:recorded_trait_count | 17 | S09: data row 5 / recorded_trait_count | identity |
| pine:cv_gblup_prediction_observed_sd_ratio_mean | 0.7786477082306693 | S09: data row 5 / cv_gblup_prediction_observed_sd_ratio_mean | identity |
| pine:cv_gblup_cb_mean | 0.963160625976531 | S09: data row 5 / cv_gblup_cb_mean | identity |
| pine:missing_percent | 0.0 | derived:pine:current_matrix_missing_fraction | percent |
| rice:cv_outer_unit_count | 10 | S09: data row 6 / cv_outer_unit_count | identity |
| rice:species | rice (Oryza sativa) | S09: data row 6 / species | identity |
| rice:n | 352 | S09: data row 6 / n | identity |
| rice:p | 27232 | S09: data row 6 / p | identity |
| rice:p_over_n | 77.36363636363636 | S09: data row 6 / p_over_n | identity |
| rice:genotype_encoding | 0/1/2 additive genotype encoding | S09: data row 6 / genotype_encoding | identity |
| rice:current_matrix_missing_fraction | 0.0 | S09: data row 6 / current_matrix_missing_fraction | identity |
| rice:recorded_trait_count | 36 | S09: data row 6 / recorded_trait_count | identity |
| rice:cv_gblup_prediction_observed_sd_ratio_mean | 0.7374987743011152 | S09: data row 6 / cv_gblup_prediction_observed_sd_ratio_mean | identity |
| rice:cv_gblup_cb_mean | 0.9517057139635678 | S09: data row 6 / cv_gblup_cb_mean | identity |
| rice:missing_percent | 0.0 | derived:rice:current_matrix_missing_fraction | percent |
| wheatG:cv_outer_unit_count | 10 | S09: data row 7 / cv_outer_unit_count | identity |
| wheatG:species | bread wheat (Triticum aestivum) | S09: data row 7 / species | identity |
| wheatG:n | 371 | S09: data row 7 / n | identity |
| wheatG:p | 12546 | S09: data row 7 / p | identity |
| wheatG:p_over_n | 33.8167115902965 | S09: data row 7 / p_over_n | identity |
| wheatG:genotype_encoding | numeric dosage; includes non-integer SVD-imputed values | S09: data row 7 / genotype_encoding | identity |
| wheatG:current_matrix_missing_fraction | 0.0 | S09: data row 7 / current_matrix_missing_fraction | identity |
| wheatG:recorded_trait_count | 16 | S09: data row 7 / recorded_trait_count | identity |
| wheatG:cv_gblup_prediction_observed_sd_ratio_mean | 0.6796856638577733 | S09: data row 7 / cv_gblup_prediction_observed_sd_ratio_mean | identity |
| wheatG:cv_gblup_cb_mean | 0.9118641085018796 | S09: data row 7 / cv_gblup_cb_mean | identity |
| wheatG:missing_percent | 0.0 | derived:wheatG:current_matrix_missing_fraction | percent |

### Table III

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| AUS2015:PCC:GBLUP | 0.809198235100852 | S15: data row 5 / control_pcc | identity |
| AUS2015:PCC:GBLUP:configuration | E6H::GBLUP_rrBLUP_mean | S15: data row 5 / control | identity |
| AUS2015:PCC:BayesB | 0.8126227083210198 | S15: data row 78 / control_pcc | identity |
| AUS2015:PCC:BayesB:configuration | HF1_E6::BayesB_long_s43 | S15: data row 78 / control | identity |
| AUS2015:PCC:Ridge | 0.7862583769306725 | S15: data row 71 / control_pcc | identity |
| AUS2015:PCC:Ridge:configuration | HF1_N_tuned::Ridge | S15: data row 71 / control | identity |
| AUS2015:PCC:ElasticNet | 0.8432442858318628 | S15: data row 13 / control_pcc | identity |
| AUS2015:PCC:ElasticNet:configuration | v8_tuned::ElasticNet | S15: data row 13 / control | identity |
| AUS2015:PCC:RF | 0.8383472834131078 | S15: data row 33 / control_pcc | identity |
| AUS2015:PCC:RF:configuration | v8_tuned::RF | S15: data row 33 / control | identity |
| AUS2015:PCC:LightGBM | 0.8474795551335902 | S15: data row 23 / control_pcc | identity |
| AUS2015:PCC:LightGBM:configuration | v8_tuned::LightGBM | S15: data row 23 / control | identity |
| AUS2015:PCC:SVR-RBF | 0.8438693912749832 | S15: data row 72 / control_pcc | identity |
| AUS2015:PCC:SVR-RBF:configuration | HF1_N_tuned::SVR-RBF | S15: data row 72 / control | identity |
| AUS2015:PCC:MLP-Dual | 0.7920344461536658 | S15: data row 75 / control_pcc | identity |
| AUS2015:PCC:MLP-Dual:configuration | HF1_N_tuned::MLP-Dual | S15: data row 75 / control | identity |
| AUS2015:PCC:WheatGP | 0.8354970352696265 | S15: data row 48 / control_pcc | identity |
| AUS2015:PCC:WheatGP:configuration | deep_adapted::WheatGP | S15: data row 48 / control | identity |
| AUS2015:PCC:Cropformer | 0.7995634161136591 | S15: data row 41 / control_pcc | identity |
| AUS2015:PCC:Cropformer:configuration | deep_adapted::Cropformer | S15: data row 41 / control | identity |
| AUS2015:PCC:VMGP | 0.7499322459865941 | S15: data row 49 / control_pcc | identity |
| AUS2015:PCC:VMGP:configuration | VMGP::seed_mean | S15: data row 49 / control | identity |
| AUS2015:PCC:TabNet | 0.5629491291157459 | S15: data row 50 / control_pcc | identity |
| AUS2015:PCC:TabNet:configuration | TabNet::raw_seed_mean | S15: data row 50 / control | identity |
| AUS2015:PCC:DeepGS | 0.5067909409637317 | S15: data row 43 / control_pcc | identity |
| AUS2015:PCC:DeepGS:configuration | deep_adapted::DeepGS | S15: data row 43 / control | identity |
| AUS2015:PCC:AF | 0.8140736669547094 | S16: data row 1 / mean_prediction_pcc | identity |
| AUS2015:PCC:GBLUP:model_rank | 8 | derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:BayesB:model_rank | 7 | derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:Ridge:model_rank | 11 | derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:ElasticNet:model_rank | 3 | derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:RF:model_rank | 4 | derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:LightGBM:model_rank | 1 | derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:SVR-RBF:model_rank | 2 | derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:MLP-Dual:model_rank | 10 | derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:WheatGP:model_rank | 5 | derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:Cropformer:model_rank | 9 | derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:VMGP:model_rank | 12 | derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:TabNet:model_rank | 13 | derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:DeepGS:model_rank | 14 | derived:AUS2015:PCC:DeepGS ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:AF | rank |
| AUS2015:PCC:AF:model_rank | 6 | derived:AUS2015:PCC:AF ; derived:AUS2015:PCC:GBLUP ; derived:AUS2015:PCC:BayesB ; derived:AUS2015:PCC:Ridge ; derived:AUS2015:PCC:ElasticNet ; derived:AUS2015:PCC:RF ; derived:AUS2015:PCC:LightGBM ; derived:AUS2015:PCC:SVR-RBF ; derived:AUS2015:PCC:MLP-Dual ; derived:AUS2015:PCC:WheatGP ; derived:AUS2015:PCC:Cropformer ; derived:AUS2015:PCC:VMGP ; derived:AUS2015:PCC:TabNet ; derived:AUS2015:PCC:DeepGS | rank |
| AUS2015:CCC:GBLUP | 0.7882745039087654 | S15: data row 74 / control_ccc | identity |
| AUS2015:CCC:GBLUP:configuration | HF1_N_tuned::GBLUP | S15: data row 74 / control | identity |
| AUS2015:CCC:BayesB | 0.7927338883668763 | S15: data row 78 / control_ccc | identity |
| AUS2015:CCC:BayesB:configuration | HF1_E6::BayesB_long_s43 | S15: data row 78 / control | identity |
| AUS2015:CCC:Ridge | 0.7784149904851602 | S15: data row 71 / control_ccc | identity |
| AUS2015:CCC:Ridge:configuration | HF1_N_tuned::Ridge | S15: data row 71 / control | identity |
| AUS2015:CCC:ElasticNet | 0.8204855102979083 | S15: data row 13 / control_ccc | identity |
| AUS2015:CCC:ElasticNet:configuration | v8_tuned::ElasticNet | S15: data row 13 / control | identity |
| AUS2015:CCC:RF | 0.7723235701798475 | S15: data row 33 / control_ccc | identity |
| AUS2015:CCC:RF:configuration | v8_tuned::RF | S15: data row 33 / control | identity |
| AUS2015:CCC:LightGBM | 0.8112094402782543 | S15: data row 23 / control_ccc | identity |
| AUS2015:CCC:LightGBM:configuration | v8_tuned::LightGBM | S15: data row 23 / control | identity |
| AUS2015:CCC:SVR-RBF | 0.8088612664456947 | S15: data row 72 / control_ccc | identity |
| AUS2015:CCC:SVR-RBF:configuration | HF1_N_tuned::SVR-RBF | S15: data row 72 / control | identity |
| AUS2015:CCC:MLP-Dual | 0.7825310427313428 | S15: data row 75 / control_ccc | identity |
| AUS2015:CCC:MLP-Dual:configuration | HF1_N_tuned::MLP-Dual | S15: data row 75 / control | identity |
| AUS2015:CCC:WheatGP | 0.8139236356740269 | S15: data row 48 / control_ccc | identity |
| AUS2015:CCC:WheatGP:configuration | deep_adapted::WheatGP | S15: data row 48 / control | identity |
| AUS2015:CCC:Cropformer | 0.7650093495947775 | S15: data row 41 / control_ccc | identity |
| AUS2015:CCC:Cropformer:configuration | deep_adapted::Cropformer | S15: data row 41 / control | identity |
| AUS2015:CCC:VMGP | 0.4051530783253877 | S15: data row 49 / control_ccc | identity |
| AUS2015:CCC:VMGP:configuration | VMGP::seed_mean | S15: data row 49 / control | identity |
| AUS2015:CCC:TabNet | 0.2725865990452112 | S15: data row 50 / control_ccc | identity |
| AUS2015:CCC:TabNet:configuration | TabNet::raw_seed_mean | S15: data row 50 / control | identity |
| AUS2015:CCC:DeepGS | 0.0873608666058682 | S15: data row 43 / control_ccc | identity |
| AUS2015:CCC:DeepGS:configuration | deep_adapted::DeepGS | S15: data row 43 / control | identity |
| AUS2015:CCC:AF | 0.7800393998405797 | S16: data row 1 / mean_prediction_ccc | identity |
| AUS2015:CCC:GBLUP:model_rank | 6 | derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:BayesB:model_rank | 5 | derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:Ridge:model_rank | 9 | derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:ElasticNet:model_rank | 1 | derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:RF:model_rank | 10 | derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:LightGBM:model_rank | 3 | derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:SVR-RBF:model_rank | 4 | derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:MLP-Dual:model_rank | 7 | derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:WheatGP:model_rank | 2 | derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:Cropformer:model_rank | 11 | derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:VMGP:model_rank | 12 | derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:TabNet:model_rank | 13 | derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:DeepGS:model_rank | 14 | derived:AUS2015:CCC:DeepGS ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:AF | rank |
| AUS2015:CCC:AF:model_rank | 8 | derived:AUS2015:CCC:AF ; derived:AUS2015:CCC:GBLUP ; derived:AUS2015:CCC:BayesB ; derived:AUS2015:CCC:Ridge ; derived:AUS2015:CCC:ElasticNet ; derived:AUS2015:CCC:RF ; derived:AUS2015:CCC:LightGBM ; derived:AUS2015:CCC:SVR-RBF ; derived:AUS2015:CCC:MLP-Dual ; derived:AUS2015:CCC:WheatGP ; derived:AUS2015:CCC:Cropformer ; derived:AUS2015:CCC:VMGP ; derived:AUS2015:CCC:TabNet ; derived:AUS2015:CCC:DeepGS | rank |
| GABI:PCC:GBLUP | 0.5746805112951394 | S15: data row 55 / control_pcc | identity |
| GABI:PCC:GBLUP:configuration | E6H::GBLUP_rrBLUP_mean | S15: data row 55 / control | identity |
| GABI:PCC:BayesB | 0.6056309322783267 | S15: data row 90 / control_pcc | identity |
| GABI:PCC:BayesB:configuration | HF1_E6::BayesB_short_s43 | S15: data row 90 / control | identity |
| GABI:PCC:Ridge | 0.5725671815829038 | S15: data row 81 / control_pcc | identity |
| GABI:PCC:Ridge:configuration | HF1_N_tuned::Ridge | S15: data row 81 / control | identity |
| GABI:PCC:ElasticNet | 0.6566215301368783 | S15: data row 101 / control_pcc | identity |
| GABI:PCC:ElasticNet:configuration | HF2_v8_tuned::ElasticNet | S15: data row 101 / control | identity |
| GABI:PCC:RF | 0.6275199999356256 | S15: data row 56 / control_pcc | identity |
| GABI:PCC:RF:configuration | E6H::RF_default | S15: data row 56 / control | identity |
| GABI:PCC:LightGBM | 0.6708888316693542 | S15: data row 102 / control_pcc | identity |
| GABI:PCC:LightGBM:configuration | HF2_v8_tuned::LightGBM | S15: data row 102 / control | identity |
| GABI:PCC:SVR-RBF | 0.5940561607712205 | S15: data row 82 / control_pcc | identity |
| GABI:PCC:SVR-RBF:configuration | HF1_N_tuned::SVR-RBF | S15: data row 82 / control | identity |
| GABI:PCC:MLP-Dual | 0.4965740040611424 | S15: data row 85 / control_pcc | identity |
| GABI:PCC:MLP-Dual:configuration | HF1_N_tuned::MLP-Dual | S15: data row 85 / control | identity |
| GABI:PCC:WheatGP | 0.5735816961767792 | S15: data row 103 / control_pcc | identity |
| GABI:PCC:WheatGP:configuration | HF2_deep::WheatGP | S15: data row 103 / control | identity |
| GABI:PCC:Cropformer | 0.6049579569059158 | S15: data row 104 / control_pcc | identity |
| GABI:PCC:Cropformer:configuration | HF2_deep::Cropformer | S15: data row 104 / control | identity |
| GABI:PCC:VMGP | 0.6008456841635139 | S15: data row 59 / control_pcc | identity |
| GABI:PCC:VMGP:configuration | VMGP::seed_mean | S15: data row 59 / control | identity |
| GABI:PCC:TabNet | 0.1002039700310759 | S15: data row 60 / control_pcc | identity |
| GABI:PCC:TabNet:configuration | TabNet::raw_seed_mean | S15: data row 60 / control | identity |
| GABI:PCC:DeepGS | 0.571216628216454 | S15: data row 105 / control_pcc | identity |
| GABI:PCC:DeepGS:configuration | HF2_deep::DeepGS | S15: data row 105 / control | identity |
| GABI:PCC:AF | 0.6131458954143664 | S16: data row 2 / mean_prediction_pcc | identity |
| GABI:PCC:GBLUP:model_rank | 9 | derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:BayesB:model_rank | 5 | derived:GABI:PCC:BayesB ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:Ridge:model_rank | 11 | derived:GABI:PCC:Ridge ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:ElasticNet:model_rank | 2 | derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:RF:model_rank | 3 | derived:GABI:PCC:RF ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:LightGBM:model_rank | 1 | derived:GABI:PCC:LightGBM ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:SVR-RBF:model_rank | 8 | derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:MLP-Dual:model_rank | 13 | derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:WheatGP:model_rank | 10 | derived:GABI:PCC:WheatGP ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:Cropformer:model_rank | 6 | derived:GABI:PCC:Cropformer ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:VMGP:model_rank | 7 | derived:GABI:PCC:VMGP ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:TabNet:model_rank | 14 | derived:GABI:PCC:TabNet ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:DeepGS ; derived:GABI:PCC:AF | rank |
| GABI:PCC:DeepGS:model_rank | 12 | derived:GABI:PCC:DeepGS ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:AF | rank |
| GABI:PCC:AF:model_rank | 4 | derived:GABI:PCC:AF ; derived:GABI:PCC:GBLUP ; derived:GABI:PCC:BayesB ; derived:GABI:PCC:Ridge ; derived:GABI:PCC:ElasticNet ; derived:GABI:PCC:RF ; derived:GABI:PCC:LightGBM ; derived:GABI:PCC:SVR-RBF ; derived:GABI:PCC:MLP-Dual ; derived:GABI:PCC:WheatGP ; derived:GABI:PCC:Cropformer ; derived:GABI:PCC:VMGP ; derived:GABI:PCC:TabNet ; derived:GABI:PCC:DeepGS | rank |
| GABI:CCC:GBLUP | 0.5027696585419968 | S15: data row 55 / control_ccc | identity |
| GABI:CCC:GBLUP:configuration | E6H::GBLUP_rrBLUP_mean | S15: data row 55 / control | identity |
| GABI:CCC:BayesB | 0.5163135808855789 | S15: data row 90 / control_ccc | identity |
| GABI:CCC:BayesB:configuration | HF1_E6::BayesB_short_s43 | S15: data row 90 / control | identity |
| GABI:CCC:Ridge | 0.5032648739658225 | S15: data row 57 / control_ccc | identity |
| GABI:CCC:Ridge:configuration | E6H::Ridge_default | S15: data row 57 / control | identity |
| GABI:CCC:ElasticNet | 0.512312442746988 | S15: data row 101 / control_ccc | identity |
| GABI:CCC:ElasticNet:configuration | HF2_v8_tuned::ElasticNet | S15: data row 101 / control | identity |
| GABI:CCC:RF | 0.428885436444008 | S15: data row 56 / control_ccc | identity |
| GABI:CCC:RF:configuration | E6H::RF_default | S15: data row 56 / control | identity |
| GABI:CCC:LightGBM | 0.5440210872271313 | S15: data row 102 / control_ccc | identity |
| GABI:CCC:LightGBM:configuration | HF2_v8_tuned::LightGBM | S15: data row 102 / control | identity |
| GABI:CCC:SVR-RBF | 0.473617300577416 | S15: data row 82 / control_ccc | identity |
| GABI:CCC:SVR-RBF:configuration | HF1_N_tuned::SVR-RBF | S15: data row 82 / control | identity |
| GABI:CCC:MLP-Dual | 0.437260604674166 | S15: data row 85 / control_ccc | identity |
| GABI:CCC:MLP-Dual:configuration | HF1_N_tuned::MLP-Dual | S15: data row 85 / control | identity |
| GABI:CCC:WheatGP | 0.4522364178568989 | S15: data row 103 / control_ccc | identity |
| GABI:CCC:WheatGP:configuration | HF2_deep::WheatGP | S15: data row 103 / control | identity |
| GABI:CCC:Cropformer | 0.5961870915740501 | S15: data row 104 / control_ccc | identity |
| GABI:CCC:Cropformer:configuration | HF2_deep::Cropformer | S15: data row 104 / control | identity |
| GABI:CCC:VMGP | 0.2329141336538895 | S15: data row 59 / control_ccc | identity |
| GABI:CCC:VMGP:configuration | VMGP::seed_mean | S15: data row 59 / control | identity |
| GABI:CCC:TabNet | 0.0246272107610012 | S15: data row 60 / control_ccc | identity |
| GABI:CCC:TabNet:configuration | TabNet::raw_seed_mean | S15: data row 60 / control | identity |
| GABI:CCC:DeepGS | 0.4007375367688788 | S15: data row 105 / control_ccc | identity |
| GABI:CCC:DeepGS:configuration | HF2_deep::DeepGS | S15: data row 105 / control | identity |
| GABI:CCC:AF | 0.5829508787572862 | S16: data row 2 / mean_prediction_ccc | identity |
| GABI:CCC:GBLUP:model_rank | 7 | derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:BayesB:model_rank | 4 | derived:GABI:CCC:BayesB ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:Ridge:model_rank | 6 | derived:GABI:CCC:Ridge ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:ElasticNet:model_rank | 5 | derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:RF:model_rank | 11 | derived:GABI:CCC:RF ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:LightGBM:model_rank | 3 | derived:GABI:CCC:LightGBM ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:SVR-RBF:model_rank | 8 | derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:MLP-Dual:model_rank | 10 | derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:WheatGP:model_rank | 9 | derived:GABI:CCC:WheatGP ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:Cropformer:model_rank | 1 | derived:GABI:CCC:Cropformer ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:VMGP:model_rank | 13 | derived:GABI:CCC:VMGP ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:TabNet:model_rank | 14 | derived:GABI:CCC:TabNet ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:DeepGS ; derived:GABI:CCC:AF | rank |
| GABI:CCC:DeepGS:model_rank | 12 | derived:GABI:CCC:DeepGS ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:AF | rank |
| GABI:CCC:AF:model_rank | 2 | derived:GABI:CCC:AF ; derived:GABI:CCC:GBLUP ; derived:GABI:CCC:BayesB ; derived:GABI:CCC:Ridge ; derived:GABI:CCC:ElasticNet ; derived:GABI:CCC:RF ; derived:GABI:CCC:LightGBM ; derived:GABI:CCC:SVR-RBF ; derived:GABI:CCC:MLP-Dual ; derived:GABI:CCC:WheatGP ; derived:GABI:CCC:Cropformer ; derived:GABI:CCC:VMGP ; derived:GABI:CCC:TabNet ; derived:GABI:CCC:DeepGS | rank |
| Ward:PCC:GBLUP | 0.3970563449287299 | S15: data row 94 / control_pcc | identity |
| Ward:PCC:GBLUP:configuration | HF1_N_tuned::GBLUP | S15: data row 94 / control | identity |
| Ward:PCC:BayesB | 0.4150787437360027 | S15: data row 99 / control_pcc | identity |
| Ward:PCC:BayesB:configuration | HF1_E6::BayesB_short_s42 | S15: data row 99 / control | identity |
| Ward:PCC:Ridge | 0.3929977275428529 | S15: data row 91 / control_pcc | identity |
| Ward:PCC:Ridge:configuration | HF1_N_tuned::Ridge | S15: data row 91 / control | identity |
| Ward:PCC:ElasticNet | 0.3566381465332454 | S15: data row 106 / control_pcc | identity |
| Ward:PCC:ElasticNet:configuration | HF2_v8_tuned::ElasticNet | S15: data row 106 / control | identity |
| Ward:PCC:RF | 0.4085524099985493 | S15: data row 93 / control_pcc | identity |
| Ward:PCC:RF:configuration | HF1_N_tuned::RF | S15: data row 93 / control | identity |
| Ward:PCC:LightGBM | 0.2782831197257298 | S15: data row 107 / control_pcc | identity |
| Ward:PCC:LightGBM:configuration | HF2_v8_tuned::LightGBM | S15: data row 107 / control | identity |
| Ward:PCC:SVR-RBF | 0.4384228941453866 | S15: data row 92 / control_pcc | identity |
| Ward:PCC:SVR-RBF:configuration | HF1_N_tuned::SVR-RBF | S15: data row 92 / control | identity |
| Ward:PCC:MLP-Dual | 0.3789926389360303 | S15: data row 95 / control_pcc | identity |
| Ward:PCC:MLP-Dual:configuration | HF1_N_tuned::MLP-Dual | S15: data row 95 / control | identity |
| Ward:PCC:WheatGP | 0.3988611960134234 | S15: data row 108 / control_pcc | identity |
| Ward:PCC:WheatGP:configuration | HF2_deep::WheatGP | S15: data row 108 / control | identity |
| Ward:PCC:Cropformer | 0.394492436019718 | S15: data row 109 / control_pcc | identity |
| Ward:PCC:Cropformer:configuration | HF2_deep::Cropformer | S15: data row 109 / control | identity |
| Ward:PCC:VMGP | 0.3970366790655782 | S15: data row 96 / control_pcc | identity |
| Ward:PCC:VMGP:configuration | HF1_N_tuned::VMGP | S15: data row 96 / control | identity |
| Ward:PCC:TabNet | -0.0817704086719561 | S15: data row 70 / control_pcc | identity |
| Ward:PCC:TabNet:configuration | TabNet::raw_seed_mean | S15: data row 70 / control | identity |
| Ward:PCC:DeepGS | 0.3323847674777462 | S15: data row 110 / control_pcc | identity |
| Ward:PCC:DeepGS:configuration | HF2_deep::DeepGS | S15: data row 110 / control | identity |
| Ward:PCC:AF | 0.390014308571425 | S16: data row 3 / mean_prediction_pcc | identity |
| Ward:PCC:GBLUP:model_rank | 5 | derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:BayesB:model_rank | 2 | derived:Ward:PCC:BayesB ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:Ridge:model_rank | 8 | derived:Ward:PCC:Ridge ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:ElasticNet:model_rank | 11 | derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:RF:model_rank | 3 | derived:Ward:PCC:RF ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:LightGBM:model_rank | 13 | derived:Ward:PCC:LightGBM ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:SVR-RBF:model_rank | 1 | derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:MLP-Dual:model_rank | 10 | derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:WheatGP:model_rank | 4 | derived:Ward:PCC:WheatGP ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:Cropformer:model_rank | 7 | derived:Ward:PCC:Cropformer ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:VMGP:model_rank | 6 | derived:Ward:PCC:VMGP ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:TabNet:model_rank | 14 | derived:Ward:PCC:TabNet ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:DeepGS ; derived:Ward:PCC:AF | rank |
| Ward:PCC:DeepGS:model_rank | 12 | derived:Ward:PCC:DeepGS ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:AF | rank |
| Ward:PCC:AF:model_rank | 9 | derived:Ward:PCC:AF ; derived:Ward:PCC:GBLUP ; derived:Ward:PCC:BayesB ; derived:Ward:PCC:Ridge ; derived:Ward:PCC:ElasticNet ; derived:Ward:PCC:RF ; derived:Ward:PCC:LightGBM ; derived:Ward:PCC:SVR-RBF ; derived:Ward:PCC:MLP-Dual ; derived:Ward:PCC:WheatGP ; derived:Ward:PCC:Cropformer ; derived:Ward:PCC:VMGP ; derived:Ward:PCC:TabNet ; derived:Ward:PCC:DeepGS | rank |
| Ward:CCC:GBLUP | 0.239913441015598 | S15: data row 65 / control_ccc | identity |
| Ward:CCC:GBLUP:configuration | E6H::GBLUP_rrBLUP_mean | S15: data row 65 / control | identity |
| Ward:CCC:BayesB | 0.2818356449997946 | S15: data row 99 / control_ccc | identity |
| Ward:CCC:BayesB:configuration | HF1_E6::BayesB_short_s42 | S15: data row 99 / control | identity |
| Ward:CCC:Ridge | 0.2704866137095404 | S15: data row 91 / control_ccc | identity |
| Ward:CCC:Ridge:configuration | HF1_N_tuned::Ridge | S15: data row 91 / control | identity |
| Ward:CCC:ElasticNet | 0.2322988713062919 | S15: data row 106 / control_ccc | identity |
| Ward:CCC:ElasticNet:configuration | HF2_v8_tuned::ElasticNet | S15: data row 106 / control | identity |
| Ward:CCC:RF | 0.1732047607209005 | S15: data row 93 / control_ccc | identity |
| Ward:CCC:RF:configuration | HF1_N_tuned::RF | S15: data row 93 / control | identity |
| Ward:CCC:LightGBM | 0.1841849487778598 | S15: data row 107 / control_ccc | identity |
| Ward:CCC:LightGBM:configuration | HF2_v8_tuned::LightGBM | S15: data row 107 / control | identity |
| Ward:CCC:SVR-RBF | 0.2691457001886488 | S15: data row 92 / control_ccc | identity |
| Ward:CCC:SVR-RBF:configuration | HF1_N_tuned::SVR-RBF | S15: data row 92 / control | identity |
| Ward:CCC:MLP-Dual | 0.2921341896275597 | S15: data row 95 / control_ccc | identity |
| Ward:CCC:MLP-Dual:configuration | HF1_N_tuned::MLP-Dual | S15: data row 95 / control | identity |
| Ward:CCC:WheatGP | 0.2610547112513623 | S15: data row 108 / control_ccc | identity |
| Ward:CCC:WheatGP:configuration | HF2_deep::WheatGP | S15: data row 108 / control | identity |
| Ward:CCC:Cropformer | 0.3550649127508327 | S15: data row 109 / control_ccc | identity |
| Ward:CCC:Cropformer:configuration | HF2_deep::Cropformer | S15: data row 109 / control | identity |
| Ward:CCC:VMGP | 0.1545442297723559 | S15: data row 96 / control_ccc | identity |
| Ward:CCC:VMGP:configuration | HF1_N_tuned::VMGP | S15: data row 96 / control | identity |
| Ward:CCC:TabNet | -0.023026096683461 | S15: data row 70 / control_ccc | identity |
| Ward:CCC:TabNet:configuration | TabNet::raw_seed_mean | S15: data row 70 / control | identity |
| Ward:CCC:DeepGS | 0.1501034635734465 | S15: data row 110 / control_ccc | identity |
| Ward:CCC:DeepGS:configuration | HF2_deep::DeepGS | S15: data row 110 / control | identity |
| Ward:CCC:AF | 0.3757674271951368 | S16: data row 3 / mean_prediction_ccc | identity |
| Ward:CCC:GBLUP:model_rank | 8 | derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:BayesB:model_rank | 4 | derived:Ward:CCC:BayesB ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:Ridge:model_rank | 5 | derived:Ward:CCC:Ridge ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:ElasticNet:model_rank | 9 | derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:RF:model_rank | 11 | derived:Ward:CCC:RF ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:LightGBM:model_rank | 10 | derived:Ward:CCC:LightGBM ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:SVR-RBF:model_rank | 6 | derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:MLP-Dual:model_rank | 3 | derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:WheatGP:model_rank | 7 | derived:Ward:CCC:WheatGP ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:Cropformer:model_rank | 2 | derived:Ward:CCC:Cropformer ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:VMGP:model_rank | 12 | derived:Ward:CCC:VMGP ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:TabNet:model_rank | 14 | derived:Ward:CCC:TabNet ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:DeepGS ; derived:Ward:CCC:AF | rank |
| Ward:CCC:DeepGS:model_rank | 13 | derived:Ward:CCC:DeepGS ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:AF | rank |
| Ward:CCC:AF:model_rank | 1 | derived:Ward:CCC:AF ; derived:Ward:CCC:GBLUP ; derived:Ward:CCC:BayesB ; derived:Ward:CCC:Ridge ; derived:Ward:CCC:ElasticNet ; derived:Ward:CCC:RF ; derived:Ward:CCC:LightGBM ; derived:Ward:CCC:SVR-RBF ; derived:Ward:CCC:MLP-Dual ; derived:Ward:CCC:WheatGP ; derived:Ward:CCC:Cropformer ; derived:Ward:CCC:VMGP ; derived:Ward:CCC:TabNet ; derived:Ward:CCC:DeepGS | rank |
| AUS2015:per_seed:pcc:mean | 0.810370870976233 | S20: data row 1 / pcc ; S20: data row 2 / pcc ; S20: data row 3 / pcc ; S20: data row 4 / pcc ; S20: data row 5 / pcc ; S20: data row 6 / pcc ; S20: data row 7 / pcc ; S20: data row 8 / pcc ; S20: data row 9 / pcc ; S20: data row 10 / pcc ; S20: data row 11 / pcc ; S20: data row 12 / pcc ; S20: data row 13 / pcc ; S20: data row 14 / pcc ; S20: data row 15 / pcc ; S20: data row 16 / pcc ; S20: data row 17 / pcc ; S20: data row 18 / pcc ; S20: data row 19 / pcc ; S20: data row 20 / pcc | mean |
| AUS2015:per_seed:pcc:sd | 0.006299009422323069 | S20: data row 1 / pcc ; S20: data row 2 / pcc ; S20: data row 3 / pcc ; S20: data row 4 / pcc ; S20: data row 5 / pcc ; S20: data row 6 / pcc ; S20: data row 7 / pcc ; S20: data row 8 / pcc ; S20: data row 9 / pcc ; S20: data row 10 / pcc ; S20: data row 11 / pcc ; S20: data row 12 / pcc ; S20: data row 13 / pcc ; S20: data row 14 / pcc ; S20: data row 15 / pcc ; S20: data row 16 / pcc ; S20: data row 17 / pcc ; S20: data row 18 / pcc ; S20: data row 19 / pcc ; S20: data row 20 / pcc | std_sample |
| AUS2015:per_seed:ccc:mean | 0.7581709707132303 | S20: data row 1 / ccc ; S20: data row 2 / ccc ; S20: data row 3 / ccc ; S20: data row 4 / ccc ; S20: data row 5 / ccc ; S20: data row 6 / ccc ; S20: data row 7 / ccc ; S20: data row 8 / ccc ; S20: data row 9 / ccc ; S20: data row 10 / ccc ; S20: data row 11 / ccc ; S20: data row 12 / ccc ; S20: data row 13 / ccc ; S20: data row 14 / ccc ; S20: data row 15 / ccc ; S20: data row 16 / ccc ; S20: data row 17 / ccc ; S20: data row 18 / ccc ; S20: data row 19 / ccc ; S20: data row 20 / ccc | mean |
| AUS2015:per_seed:ccc:sd | 0.05177024778313297 | S20: data row 1 / ccc ; S20: data row 2 / ccc ; S20: data row 3 / ccc ; S20: data row 4 / ccc ; S20: data row 5 / ccc ; S20: data row 6 / ccc ; S20: data row 7 / ccc ; S20: data row 8 / ccc ; S20: data row 9 / ccc ; S20: data row 10 / ccc ; S20: data row 11 / ccc ; S20: data row 12 / ccc ; S20: data row 13 / ccc ; S20: data row 14 / ccc ; S20: data row 15 / ccc ; S20: data row 16 / ccc ; S20: data row 17 / ccc ; S20: data row 18 / ccc ; S20: data row 19 / ccc ; S20: data row 20 / ccc | std_sample |
| AUS2015:per_seed:n | 20 | S20: data row 1 / seed ; S20: data row 2 / seed ; S20: data row 3 / seed ; S20: data row 4 / seed ; S20: data row 5 / seed ; S20: data row 6 / seed ; S20: data row 7 / seed ; S20: data row 8 / seed ; S20: data row 9 / seed ; S20: data row 10 / seed ; S20: data row 11 / seed ; S20: data row 12 / seed ; S20: data row 13 / seed ; S20: data row 14 / seed ; S20: data row 15 / seed ; S20: data row 16 / seed ; S20: data row 17 / seed ; S20: data row 18 / seed ; S20: data row 19 / seed ; S20: data row 20 / seed | count |
| GABI:per_seed:pcc:mean | 0.6094074624684124 | S20: data row 61 / pcc ; S20: data row 62 / pcc ; S20: data row 63 / pcc ; S20: data row 64 / pcc ; S20: data row 65 / pcc | mean |
| GABI:per_seed:pcc:sd | 0.012084389490535096 | S20: data row 61 / pcc ; S20: data row 62 / pcc ; S20: data row 63 / pcc ; S20: data row 64 / pcc ; S20: data row 65 / pcc | std_sample |
| GABI:per_seed:ccc:mean | 0.5777850171162917 | S20: data row 61 / ccc ; S20: data row 62 / ccc ; S20: data row 63 / ccc ; S20: data row 64 / ccc ; S20: data row 65 / ccc | mean |
| GABI:per_seed:ccc:sd | 0.01808381001776078 | S20: data row 61 / ccc ; S20: data row 62 / ccc ; S20: data row 63 / ccc ; S20: data row 64 / ccc ; S20: data row 65 / ccc | std_sample |
| GABI:per_seed:n | 5 | S20: data row 61 / seed ; S20: data row 62 / seed ; S20: data row 63 / seed ; S20: data row 64 / seed ; S20: data row 65 / seed | count |
| Ward:per_seed:pcc:mean | 0.3881191358815059 | S20: data row 76 / pcc ; S20: data row 77 / pcc ; S20: data row 78 / pcc ; S20: data row 79 / pcc ; S20: data row 80 / pcc | mean |
| Ward:per_seed:pcc:sd | 0.024455999321954584 | S20: data row 76 / pcc ; S20: data row 77 / pcc ; S20: data row 78 / pcc ; S20: data row 79 / pcc ; S20: data row 80 / pcc | std_sample |
| Ward:per_seed:ccc:mean | 0.3725959674922588 | S20: data row 76 / ccc ; S20: data row 77 / ccc ; S20: data row 78 / ccc ; S20: data row 79 / ccc ; S20: data row 80 / ccc | mean |
| Ward:per_seed:ccc:sd | 0.026196326601352675 | S20: data row 76 / ccc ; S20: data row 77 / ccc ; S20: data row 78 / ccc ; S20: data row 79 / ccc ; S20: data row 80 / ccc | std_sample |
| Ward:per_seed:n | 5 | S20: data row 76 / seed ; S20: data row 77 / seed ; S20: data row 78 / seed ; S20: data row 79 / seed ; S20: data row 80 / seed | count |

### Table IV

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| w/o SBV:MLP-Dual:AUS2015 | 0.0025030878251394 | S08: data row 2 / mean_delta | identity |
| w/o SBV:MLP-Dual:AUS2015:pass | False | S08: data row 2 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:MLP-Dual:GABI | 0.0244020034777104 | S08: data row 6 / mean_delta | identity |
| w/o SBV:MLP-Dual:GABI:pass | True | S08: data row 6 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:MLP-Dual:Ward | 0.0511551180493126 | S08: data row 10 / mean_delta | identity |
| w/o SBV:MLP-Dual:Ward:pass | True | S08: data row 10 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:MLP-Dual:lentil | 0.0097943375080074 | S08: data row 14 / mean_delta | identity |
| w/o SBV:MLP-Dual:lentil:pass | False | S08: data row 14 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:MLP-Dual:pine | 0.0137220276982281 | S08: data row 18 / mean_delta | identity |
| w/o SBV:MLP-Dual:pine:pass | False | S08: data row 18 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:MLP-Dual:rice | 0.0142066462575715 | S08: data row 22 / mean_delta | identity |
| w/o SBV:MLP-Dual:rice:pass | False | S08: data row 22 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:MLP-Dual:wheatG | 0.0370302100411742 | S08: data row 26 / mean_delta | identity |
| w/o SBV:MLP-Dual:wheatG:pass | True | S08: data row 26 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:MLP-Dual:mean | 0.021830490122449087 | derived:w/o SBV:MLP-Dual:AUS2015 ; derived:w/o SBV:MLP-Dual:GABI ; derived:w/o SBV:MLP-Dual:Ward ; derived:w/o SBV:MLP-Dual:lentil ; derived:w/o SBV:MLP-Dual:pine ; derived:w/o SBV:MLP-Dual:rice ; derived:w/o SBV:MLP-Dual:wheatG | mean |
| w/o SBV:MLP-Dual:established | 3 | derived:w/o SBV:MLP-Dual:AUS2015:pass ; derived:w/o SBV:MLP-Dual:GABI:pass ; derived:w/o SBV:MLP-Dual:Ward:pass ; derived:w/o SBV:MLP-Dual:lentil:pass ; derived:w/o SBV:MLP-Dual:pine:pass ; derived:w/o SBV:MLP-Dual:rice:pass ; derived:w/o SBV:MLP-Dual:wheatG:pass | count_equal {"target": true} |
| w/o SBV:MLP-Dual:datasets | 7 | derived:w/o SBV:MLP-Dual:AUS2015 ; derived:w/o SBV:MLP-Dual:GABI ; derived:w/o SBV:MLP-Dual:Ward ; derived:w/o SBV:MLP-Dual:lentil ; derived:w/o SBV:MLP-Dual:pine ; derived:w/o SBV:MLP-Dual:rice ; derived:w/o SBV:MLP-Dual:wheatG | count |
| w/o SBV:Ridge:AUS2015 | -0.0015427941231253 | S08: data row 30 / mean_delta | identity |
| w/o SBV:Ridge:AUS2015:pass | False | S08: data row 30 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:Ridge:GABI | 0.0038798220955142 | S08: data row 34 / mean_delta | identity |
| w/o SBV:Ridge:GABI:pass | False | S08: data row 34 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:Ridge:Ward | 0.0061861179070083 | S08: data row 38 / mean_delta | identity |
| w/o SBV:Ridge:Ward:pass | False | S08: data row 38 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:Ridge:lentil | 0.0015596898142084 | S08: data row 42 / mean_delta | identity |
| w/o SBV:Ridge:lentil:pass | False | S08: data row 42 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:Ridge:pine | 0.005962838369354 | S08: data row 46 / mean_delta | identity |
| w/o SBV:Ridge:pine:pass | False | S08: data row 46 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:Ridge:rice | -0.0002216340879263 | S08: data row 50 / mean_delta | identity |
| w/o SBV:Ridge:rice:pass | False | S08: data row 50 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:Ridge:wheatG | -0.0015203611192391 | S08: data row 54 / mean_delta | identity |
| w/o SBV:Ridge:wheatG:pass | False | S08: data row 54 / decision | count_equal {"target": "ESTABLISHED"} |
| w/o SBV:Ridge:mean | 0.002043382693684886 | derived:w/o SBV:Ridge:AUS2015 ; derived:w/o SBV:Ridge:GABI ; derived:w/o SBV:Ridge:Ward ; derived:w/o SBV:Ridge:lentil ; derived:w/o SBV:Ridge:pine ; derived:w/o SBV:Ridge:rice ; derived:w/o SBV:Ridge:wheatG | mean |
| w/o SBV:Ridge:established | 0 | derived:w/o SBV:Ridge:AUS2015:pass ; derived:w/o SBV:Ridge:GABI:pass ; derived:w/o SBV:Ridge:Ward:pass ; derived:w/o SBV:Ridge:lentil:pass ; derived:w/o SBV:Ridge:pine:pass ; derived:w/o SBV:Ridge:rice:pass ; derived:w/o SBV:Ridge:wheatG:pass | count_equal {"target": true} |
| w/o SBV:Ridge:datasets | 7 | derived:w/o SBV:Ridge:AUS2015 ; derived:w/o SBV:Ridge:GABI ; derived:w/o SBV:Ridge:Ward ; derived:w/o SBV:Ridge:lentil ; derived:w/o SBV:Ridge:pine ; derived:w/o SBV:Ridge:rice ; derived:w/o SBV:Ridge:wheatG | count |
| w/o SBV:AF:AUS2015 | 0.09196625946172408 | S07: JSON ["rules", "R-K5-CONTEXT", "ccc_population", "mean"] | identity |
| w/o SBV:AF:AUS2015:decision | established | S07: JSON ["rules", "R-K5-CONTEXT", "ccc_population", "decision"] | identity |
| w/o SBV:AF:AUS2015:pass | 1 | derived:w/o SBV:AF:AUS2015:decision | count_equal {"target": "established"} |
| w/o SBV:AF:GABI | 0.2581710845147639 | S28: JSON ["rules", "R-K5-K5", "ccc_population", "datasets", "GABI", "mean"] | identity |
| w/o SBV:AF:GABI:pass | True | S28: JSON ["rules", "R-K5-K5", "ccc_population", "datasets", "GABI", "passes"] | identity |
| w/o SBV:AF:Ward | 0.2813123756504808 | S28: JSON ["rules", "R-K5-K5", "ccc_population", "datasets", "Ward", "mean"] | identity |
| w/o SBV:AF:Ward:pass | True | S28: JSON ["rules", "R-K5-K5", "ccc_population", "datasets", "Ward", "passes"] | identity |
| w/o SBV:AF:lentil | 0.227380460554303 | S23: data row 13 / mean_D | identity |
| w/o SBV:AF:lentil:pass | 1 | S23: data row 13 / decision | count_equal {"target": "PLS established"} |
| w/o SBV:AF:pine | 0.5281087408257796 | S23: data row 15 / mean_D | identity |
| w/o SBV:AF:pine:pass | 1 | S23: data row 15 / decision | count_equal {"target": "PLS established"} |
| w/o SBV:AF:rice | 0.4387757005288546 | S23: data row 17 / mean_D | identity |
| w/o SBV:AF:rice:pass | 1 | S23: data row 17 / decision | count_equal {"target": "PLS established"} |
| w/o SBV:AF:wheatG | 0.5291755445496369 | S23: data row 19 / mean_D | identity |
| w/o SBV:AF:wheatG:pass | 1 | S23: data row 19 / decision | count_equal {"target": "PLS established"} |
| w/o SBV:AF:mean | 0.3364128808693633 | derived:w/o SBV:AF:AUS2015 ; derived:w/o SBV:AF:GABI ; derived:w/o SBV:AF:Ward ; derived:w/o SBV:AF:lentil ; derived:w/o SBV:AF:pine ; derived:w/o SBV:AF:rice ; derived:w/o SBV:AF:wheatG | mean |
| w/o SBV:AF:established | 7 | derived:w/o SBV:AF:AUS2015:pass ; derived:w/o SBV:AF:GABI:pass ; derived:w/o SBV:AF:Ward:pass ; derived:w/o SBV:AF:lentil:pass ; derived:w/o SBV:AF:pine:pass ; derived:w/o SBV:AF:rice:pass ; derived:w/o SBV:AF:wheatG:pass | count_equal {"target": true} |
| w/o SBV:AF:datasets | 7 | derived:w/o SBV:AF:AUS2015 ; derived:w/o SBV:AF:GABI ; derived:w/o SBV:AF:Ward ; derived:w/o SBV:AF:lentil ; derived:w/o SBV:AF:pine ; derived:w/o SBV:AF:rice ; derived:w/o SBV:AF:wheatG | count |
| SBV to PCA:MLP-Dual:AUS2015 | 0.0126664965992631 | S08: data row 1 / mean_delta | identity |
| SBV to PCA:MLP-Dual:AUS2015:pass | True | S08: data row 1 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:MLP-Dual:GABI | 0.0085933600469731 | S08: data row 5 / mean_delta | identity |
| SBV to PCA:MLP-Dual:GABI:pass | False | S08: data row 5 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:MLP-Dual:Ward | 0.0523253847998145 | S08: data row 9 / mean_delta | identity |
| SBV to PCA:MLP-Dual:Ward:pass | True | S08: data row 9 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:MLP-Dual:lentil | 0.0107903728275283 | S08: data row 13 / mean_delta | identity |
| SBV to PCA:MLP-Dual:lentil:pass | True | S08: data row 13 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:MLP-Dual:pine | 0.0058950132361159 | S08: data row 17 / mean_delta | identity |
| SBV to PCA:MLP-Dual:pine:pass | False | S08: data row 17 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:MLP-Dual:rice | -0.0095947551096247 | S08: data row 21 / mean_delta | identity |
| SBV to PCA:MLP-Dual:rice:pass | False | S08: data row 21 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:MLP-Dual:wheatG | 0.0139500765074203 | S08: data row 25 / mean_delta | identity |
| SBV to PCA:MLP-Dual:wheatG:pass | True | S08: data row 25 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:MLP-Dual:mean | 0.013517992701070073 | derived:SBV to PCA:MLP-Dual:AUS2015 ; derived:SBV to PCA:MLP-Dual:GABI ; derived:SBV to PCA:MLP-Dual:Ward ; derived:SBV to PCA:MLP-Dual:lentil ; derived:SBV to PCA:MLP-Dual:pine ; derived:SBV to PCA:MLP-Dual:rice ; derived:SBV to PCA:MLP-Dual:wheatG | mean |
| SBV to PCA:MLP-Dual:established | 4 | derived:SBV to PCA:MLP-Dual:AUS2015:pass ; derived:SBV to PCA:MLP-Dual:GABI:pass ; derived:SBV to PCA:MLP-Dual:Ward:pass ; derived:SBV to PCA:MLP-Dual:lentil:pass ; derived:SBV to PCA:MLP-Dual:pine:pass ; derived:SBV to PCA:MLP-Dual:rice:pass ; derived:SBV to PCA:MLP-Dual:wheatG:pass | count_equal {"target": true} |
| SBV to PCA:MLP-Dual:datasets | 7 | derived:SBV to PCA:MLP-Dual:AUS2015 ; derived:SBV to PCA:MLP-Dual:GABI ; derived:SBV to PCA:MLP-Dual:Ward ; derived:SBV to PCA:MLP-Dual:lentil ; derived:SBV to PCA:MLP-Dual:pine ; derived:SBV to PCA:MLP-Dual:rice ; derived:SBV to PCA:MLP-Dual:wheatG | count |
| SBV to PCA:Ridge:AUS2015 | -0.0015869860428434 | S08: data row 29 / mean_delta | identity |
| SBV to PCA:Ridge:AUS2015:pass | False | S08: data row 29 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:Ridge:GABI | 0.0039063444058784 | S08: data row 33 / mean_delta | identity |
| SBV to PCA:Ridge:GABI:pass | False | S08: data row 33 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:Ridge:Ward | 0.0062790795559687 | S08: data row 37 / mean_delta | identity |
| SBV to PCA:Ridge:Ward:pass | False | S08: data row 37 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:Ridge:lentil | 0.0015872754015109 | S08: data row 41 / mean_delta | identity |
| SBV to PCA:Ridge:lentil:pass | False | S08: data row 41 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:Ridge:pine | 0.0059221579119251 | S08: data row 45 / mean_delta | identity |
| SBV to PCA:Ridge:pine:pass | False | S08: data row 45 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:Ridge:rice | -0.0001938192434942 | S08: data row 49 / mean_delta | identity |
| SBV to PCA:Ridge:rice:pass | False | S08: data row 49 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:Ridge:wheatG | -0.0016653156749243 | S08: data row 53 / mean_delta | identity |
| SBV to PCA:Ridge:wheatG:pass | False | S08: data row 53 / decision | count_equal {"target": "ESTABLISHED"} |
| SBV to PCA:Ridge:mean | 0.002035533759145886 | derived:SBV to PCA:Ridge:AUS2015 ; derived:SBV to PCA:Ridge:GABI ; derived:SBV to PCA:Ridge:Ward ; derived:SBV to PCA:Ridge:lentil ; derived:SBV to PCA:Ridge:pine ; derived:SBV to PCA:Ridge:rice ; derived:SBV to PCA:Ridge:wheatG | mean |
| SBV to PCA:Ridge:established | 0 | derived:SBV to PCA:Ridge:AUS2015:pass ; derived:SBV to PCA:Ridge:GABI:pass ; derived:SBV to PCA:Ridge:Ward:pass ; derived:SBV to PCA:Ridge:lentil:pass ; derived:SBV to PCA:Ridge:pine:pass ; derived:SBV to PCA:Ridge:rice:pass ; derived:SBV to PCA:Ridge:wheatG:pass | count_equal {"target": true} |
| SBV to PCA:Ridge:datasets | 7 | derived:SBV to PCA:Ridge:AUS2015 ; derived:SBV to PCA:Ridge:GABI ; derived:SBV to PCA:Ridge:Ward ; derived:SBV to PCA:Ridge:lentil ; derived:SBV to PCA:Ridge:pine ; derived:SBV to PCA:Ridge:rice ; derived:SBV to PCA:Ridge:wheatG | count |
| SBV to PCA:AF:AUS2015 | 0.05202301632419086 | S07: JSON ["rules", "v13m-R1", "ccc_population", "mean"] | identity |
| SBV to PCA:AF:AUS2015:decision | established | S07: JSON ["rules", "v13m-R1", "ccc_population", "decision"] | identity |
| SBV to PCA:AF:AUS2015:pass | 1 | derived:SBV to PCA:AF:AUS2015:decision | count_equal {"target": "established"} |
| SBV to PCA:AF:GABI | 0.13033975116327695 | S29: JSON ["arms", "R1", "datasets", "GABI", "ccc_population", "mean_D"] | identity |
| SBV to PCA:AF:GABI:pass | True | S29: JSON ["arms", "R1", "datasets", "GABI", "ccc_population", "established"] | identity |
| SBV to PCA:AF:Ward | 0.17881949466688343 | S29: JSON ["arms", "R1", "datasets", "Ward", "ccc_population", "mean_D"] | identity |
| SBV to PCA:AF:Ward:pass | True | S29: JSON ["arms", "R1", "datasets", "Ward", "ccc_population", "established"] | identity |
| SBV to PCA:AF:lentil | 0.0766429613838726 | S23: data row 3 / mean_D | identity |
| SBV to PCA:AF:lentil:pass | 1 | S23: data row 3 / decision | count_equal {"target": "PLS established"} |
| SBV to PCA:AF:pine | 0.156945966099418 | S23: data row 5 / mean_D | identity |
| SBV to PCA:AF:pine:pass | 1 | S23: data row 5 / decision | count_equal {"target": "PLS established"} |
| SBV to PCA:AF:rice | 0.0556243990687484 | S23: data row 7 / mean_D | identity |
| SBV to PCA:AF:rice:pass | 1 | S23: data row 7 / decision | count_equal {"target": "PLS established"} |
| SBV to PCA:AF:wheatG | 0.1200762309007779 | S23: data row 9 / mean_D | identity |
| SBV to PCA:AF:wheatG:pass | 1 | S23: data row 9 / decision | count_equal {"target": "PLS established"} |
| SBV to PCA:AF:mean | 0.11006740280102402 | derived:SBV to PCA:AF:AUS2015 ; derived:SBV to PCA:AF:GABI ; derived:SBV to PCA:AF:Ward ; derived:SBV to PCA:AF:lentil ; derived:SBV to PCA:AF:pine ; derived:SBV to PCA:AF:rice ; derived:SBV to PCA:AF:wheatG | mean |
| SBV to PCA:AF:established | 7 | derived:SBV to PCA:AF:AUS2015:pass ; derived:SBV to PCA:AF:GABI:pass ; derived:SBV to PCA:AF:Ward:pass ; derived:SBV to PCA:AF:lentil:pass ; derived:SBV to PCA:AF:pine:pass ; derived:SBV to PCA:AF:rice:pass ; derived:SBV to PCA:AF:wheatG:pass | count_equal {"target": true} |
| SBV to PCA:AF:datasets | 7 | derived:SBV to PCA:AF:AUS2015 ; derived:SBV to PCA:AF:GABI ; derived:SBV to PCA:AF:Ward ; derived:SBV to PCA:AF:lentil ; derived:SBV to PCA:AF:pine ; derived:SBV to PCA:AF:rice ; derived:SBV to PCA:AF:wheatG | count |
| w/o TAS:AF:AUS2015 | 0.0686853370076369 | S10: data row 1 / delta_ccc_mean | identity |
| w/o TAS:AF:AUS2015:positive | 0.7333333333333333 | S10: data row 1 / delta_ccc_positive_fraction | identity |
| w/o TAS:AF:AUS2015:pass | True | derived:w/o TAS:AF:AUS2015 ; derived:w/o TAS:AF:AUS2015:positive | criterion {"min_delta": 0.01, "min_positive": 0.6} |
| w/o TAS:AF:GABI | 0.1313976984400708 | S10: data row 4 / delta_ccc_mean | identity |
| w/o TAS:AF:GABI:positive | 0.9333333333333332 | S10: data row 4 / delta_ccc_positive_fraction | identity |
| w/o TAS:AF:GABI:pass | True | derived:w/o TAS:AF:GABI ; derived:w/o TAS:AF:GABI:positive | criterion {"min_delta": 0.01, "min_positive": 0.6} |
| w/o TAS:AF:Ward | 0.0521369225816495 | S10: data row 7 / delta_ccc_mean | identity |
| w/o TAS:AF:Ward:positive | 0.9333333333333332 | S10: data row 7 / delta_ccc_positive_fraction | identity |
| w/o TAS:AF:Ward:pass | True | derived:w/o TAS:AF:Ward ; derived:w/o TAS:AF:Ward:positive | criterion {"min_delta": 0.01, "min_positive": 0.6} |
| w/o TAS:AF:lentil | 0.08768866702615745 | S30: JSON ["C", "decisions", 6, "mean_delta"] | identity |
| w/o TAS:AF:lentil:pass | True | S30: JSON ["C", "decisions", 6, "passed"] | identity |
| w/o TAS:AF:pine | 0.14108779429405066 | S30: JSON ["C", "decisions", 7, "mean_delta"] | identity |
| w/o TAS:AF:pine:pass | True | S30: JSON ["C", "decisions", 7, "passed"] | identity |
| w/o TAS:AF:rice | 0.07017933938387569 | S30: JSON ["C", "decisions", 8, "mean_delta"] | identity |
| w/o TAS:AF:rice:pass | True | S30: JSON ["C", "decisions", 8, "passed"] | identity |
| w/o TAS:AF:wheatG | 0.16459408350473387 | S30: JSON ["C", "decisions", 9, "mean_delta"] | identity |
| w/o TAS:AF:wheatG:pass | True | S30: JSON ["C", "decisions", 9, "passed"] | identity |
| w/o TAS:AF:mean | 0.10225283460545355 | derived:w/o TAS:AF:AUS2015 ; derived:w/o TAS:AF:GABI ; derived:w/o TAS:AF:Ward ; derived:w/o TAS:AF:lentil ; derived:w/o TAS:AF:pine ; derived:w/o TAS:AF:rice ; derived:w/o TAS:AF:wheatG | mean |
| w/o TAS:AF:established | 7 | derived:w/o TAS:AF:AUS2015:pass ; derived:w/o TAS:AF:GABI:pass ; derived:w/o TAS:AF:Ward:pass ; derived:w/o TAS:AF:lentil:pass ; derived:w/o TAS:AF:pine:pass ; derived:w/o TAS:AF:rice:pass ; derived:w/o TAS:AF:wheatG:pass | count_equal {"target": true} |
| w/o TAS:AF:datasets | 7 | derived:w/o TAS:AF:AUS2015 ; derived:w/o TAS:AF:GABI ; derived:w/o TAS:AF:Ward ; derived:w/o TAS:AF:lentil ; derived:w/o TAS:AF:pine ; derived:w/o TAS:AF:rice ; derived:w/o TAS:AF:wheatG | count |
| TAS to linear:AF:AUS2015 | 0.015464351064334015 | S07: JSON ["rules", "R-K2-linear", "ccc_population", "mean"] | identity |
| TAS to linear:AF:AUS2015:decision | not_established | S07: JSON ["rules", "R-K2-linear", "ccc_population", "decision"] | identity |
| TAS to linear:AF:AUS2015:pass | 0 | derived:TAS to linear:AF:AUS2015:decision | count_equal {"target": "established"} |
| TAS to linear:AF:GABI | 0.1264729579605271 | S10: data row 5 / delta_ccc_mean | identity |
| TAS to linear:AF:GABI:positive | 1.0 | S10: data row 5 / delta_ccc_positive_fraction | identity |
| TAS to linear:AF:GABI:pass | True | derived:TAS to linear:AF:GABI ; derived:TAS to linear:AF:GABI:positive | criterion {"min_delta": 0.01, "min_positive": 0.6} |
| TAS to linear:AF:Ward | 0.1492541701044955 | S10: data row 8 / delta_ccc_mean | identity |
| TAS to linear:AF:Ward:positive | 1.0 | S10: data row 8 / delta_ccc_positive_fraction | identity |
| TAS to linear:AF:Ward:pass | True | derived:TAS to linear:AF:Ward ; derived:TAS to linear:AF:Ward:positive | criterion {"min_delta": 0.01, "min_positive": 0.6} |
| TAS to linear:AF:mean | 0.09706382637645221 | derived:TAS to linear:AF:AUS2015 ; derived:TAS to linear:AF:GABI ; derived:TAS to linear:AF:Ward | mean |
| TAS to linear:AF:established | 2 | derived:TAS to linear:AF:AUS2015:pass ; derived:TAS to linear:AF:GABI:pass ; derived:TAS to linear:AF:Ward:pass | count_equal {"target": true} |
| TAS to linear:AF:datasets | 3 | derived:TAS to linear:AF:AUS2015 ; derived:TAS to linear:AF:GABI ; derived:TAS to linear:AF:Ward | count |
| w/o TAS:MLP-Dual:AUS2015 | -0.002353088131642441 | S12: JSON ["R-K8", "ccc_population", "datasets", "AUS2015", "mean"] | identity |
| w/o TAS:MLP-Dual:AUS2015:pass | False | S12: JSON ["R-K8", "ccc_population", "datasets", "AUS2015", "passes"] | identity |
| w/o TAS:MLP-Dual:GABI | -0.020903115973044773 | S12: JSON ["R-K8", "ccc_population", "datasets", "GABI", "mean"] | identity |
| w/o TAS:MLP-Dual:GABI:pass | False | S12: JSON ["R-K8", "ccc_population", "datasets", "GABI", "passes"] | identity |
| w/o TAS:MLP-Dual:Ward | -0.009724225253565184 | S12: JSON ["R-K8", "ccc_population", "datasets", "Ward", "mean"] | identity |
| w/o TAS:MLP-Dual:Ward:pass | False | S12: JSON ["R-K8", "ccc_population", "datasets", "Ward", "passes"] | identity |
| w/o TAS:MLP-Dual:mean | -0.010993476452750799 | derived:w/o TAS:MLP-Dual:AUS2015 ; derived:w/o TAS:MLP-Dual:GABI ; derived:w/o TAS:MLP-Dual:Ward | mean |
| w/o TAS:MLP-Dual:established | 0 | derived:w/o TAS:MLP-Dual:AUS2015:pass ; derived:w/o TAS:MLP-Dual:GABI:pass ; derived:w/o TAS:MLP-Dual:Ward:pass | count_equal {"target": true} |
| w/o TAS:MLP-Dual:datasets | 3 | derived:w/o TAS:MLP-Dual:AUS2015 ; derived:w/o TAS:MLP-Dual:GABI ; derived:w/o TAS:MLP-Dual:Ward | count |
| Perm:AUS2015:MT:median | 0.776251823881322 | S21: data row 2 / median | identity |
| Perm:AUS2015:MT:n_seeds | 20 | S21: data row 2 / n_seeds | identity |
| Perm:AUS2015:Perm:median | 0.7628499610835988 | S21: data row 4 / median | identity |
| Perm:AUS2015:Perm:n_seeds | 20 | S21: data row 4 / n_seeds | identity |
| Perm:AUS2015:ST:median | 0.6470578297584235 | S21: data row 6 / median | identity |
| Perm:AUS2015:ST:n_seeds | 20 | S21: data row 6 / n_seeds | identity |
| Perm:AUS2015:difference_of_medians | 0.013401862797723152 | derived:Perm:AUS2015:MT:median ; derived:Perm:AUS2015:Perm:median | subtract |
| Perm:AUS2015:retained_numerator | 0.1157921313251753 | derived:Perm:AUS2015:Perm:median ; derived:Perm:AUS2015:ST:median | subtract |
| Perm:AUS2015:retained_denominator | 0.12919399412289845 | derived:Perm:AUS2015:MT:median ; derived:Perm:AUS2015:ST:median | subtract |
| Perm:AUS2015:retained | 0.8962655896761397 | derived:Perm:AUS2015:retained_numerator ; derived:Perm:AUS2015:retained_denominator | divide |
| Perm:GABI:MT:median | 0.5715150604682252 | S21: data row 8 / median | identity |
| Perm:GABI:MT:n_seeds | 5 | S21: data row 8 / n_seeds | identity |
| Perm:GABI:Perm:median | 0.5591518799796408 | S21: data row 10 / median | identity |
| Perm:GABI:Perm:n_seeds | 5 | S21: data row 10 / n_seeds | identity |
| Perm:GABI:ST:median | 0.3469739203306358 | S21: data row 12 / median | identity |
| Perm:GABI:ST:n_seeds | 5 | S21: data row 12 / n_seeds | identity |
| Perm:GABI:difference_of_medians | 0.012363180488584424 | derived:Perm:GABI:MT:median ; derived:Perm:GABI:Perm:median | subtract |
| Perm:GABI:retained_numerator | 0.212177959649005 | derived:Perm:GABI:Perm:median ; derived:Perm:GABI:ST:median | subtract |
| Perm:GABI:retained_denominator | 0.2245411401375894 | derived:Perm:GABI:MT:median ; derived:Perm:GABI:ST:median | subtract |
| Perm:GABI:retained | 0.9449402435517661 | derived:Perm:GABI:retained_numerator ; derived:Perm:GABI:retained_denominator | divide |
| Perm:Ward:MT:median | 0.3719191980062401 | S21: data row 14 / median | identity |
| Perm:Ward:MT:n_seeds | 5 | S21: data row 14 / n_seeds | identity |
| Perm:Ward:Perm:median | 0.3350706635841684 | S21: data row 16 / median | identity |
| Perm:Ward:Perm:n_seeds | 5 | S21: data row 16 / n_seeds | identity |
| Perm:Ward:ST:median | 0.3065028454231898 | S21: data row 18 / median | identity |
| Perm:Ward:ST:n_seeds | 5 | S21: data row 18 / n_seeds | identity |
| Perm:Ward:difference_of_medians | 0.0368485344220717 | derived:Perm:Ward:MT:median ; derived:Perm:Ward:Perm:median | subtract |
| Perm:Ward:retained_numerator | 0.028567818160978642 | derived:Perm:Ward:Perm:median ; derived:Perm:Ward:ST:median | subtract |
| Perm:Ward:retained_denominator | 0.06541635258305034 | derived:Perm:Ward:MT:median ; derived:Perm:Ward:ST:median | subtract |
| Perm:Ward:retained | 0.43670759730466363 | derived:Perm:Ward:retained_numerator ; derived:Perm:Ward:retained_denominator | divide |
| Perm:mean_difference_of_medians | 0.020871192569459757 | derived:Perm:AUS2015:difference_of_medians ; derived:Perm:GABI:difference_of_medians ; derived:Perm:Ward:difference_of_medians | mean |

### Fig. 3

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| AUS2015:mean_delta_ln_pcc | 0.0052121414953643 | S22: data row 1 / mean_delta_ln_pcc | identity |
| AUS2015:mean_delta_ln_cb | 0.1089866860603288 | S22: data row 1 / mean_delta_ln_cb | identity |
| AUS2015:mean_delta_ccc | 0.0686853370076369 | S22: data row 1 / mean_delta_ccc | identity |
| AUS2015:n_units | 15 | S22: data row 1 / n_units | identity |
| AUS2015:protocol | v13k K | S22: data row 1 / protocol | identity |
| AUS2015:delta_ln_ccc | 0.11419882755569309 | derived:AUS2015:mean_delta_ln_pcc ; derived:AUS2015:mean_delta_ln_cb | sum |
| GABI:mean_delta_ln_pcc | -0.0086106089474388 | S22: data row 2 / mean_delta_ln_pcc | identity |
| GABI:mean_delta_ln_cb | 0.618246167048275 | S22: data row 2 / mean_delta_ln_cb | identity |
| GABI:mean_delta_ccc | 0.2649093571949064 | S22: data row 2 / mean_delta_ccc | identity |
| GABI:n_units | 15 | S22: data row 2 / n_units | identity |
| GABI:protocol | v13k K | S22: data row 2 / protocol | identity |
| GABI:delta_ln_ccc | 0.6096355581008361 | derived:GABI:mean_delta_ln_pcc ; derived:GABI:mean_delta_ln_cb | sum |
| Ward:mean_delta_ln_pcc | -0.104151226286046 | S22: data row 3 / mean_delta_ln_pcc | identity |
| Ward:mean_delta_ln_cb | 0.3483561799772098 | S22: data row 3 / mean_delta_ln_cb | identity |
| Ward:mean_delta_ccc | 0.0706018595827842 | S22: data row 3 / mean_delta_ccc | identity |
| Ward:n_units | 15 | S22: data row 3 / n_units | identity |
| Ward:protocol | v13k K | S22: data row 3 / protocol | identity |
| Ward:delta_ln_ccc | 0.2442049536911638 | derived:Ward:mean_delta_ln_pcc ; derived:Ward:mean_delta_ln_cb | sum |
| lentil:mean_delta_ln_pcc | -0.0034599819982524 | S22: data row 5 / mean_delta_ln_pcc | identity |
| lentil:mean_delta_ln_cb | 0.1315808058901391 | S22: data row 5 / mean_delta_ln_cb | identity |
| lentil:mean_delta_ccc | 0.0876886670261574 | S22: data row 5 / mean_delta_ccc | identity |
| lentil:n_units | 10 | S22: data row 5 / n_units | identity |
| lentil:protocol | v13o O | S22: data row 5 / protocol | identity |
| lentil:delta_ln_ccc | 0.1281208238918867 | derived:lentil:mean_delta_ln_pcc ; derived:lentil:mean_delta_ln_cb | sum |
| pine:mean_delta_ln_pcc | 0.0155442303877511 | S22: data row 6 / mean_delta_ln_pcc | identity |
| pine:mean_delta_ln_cb | 0.1994901815931389 | S22: data row 6 / mean_delta_ln_cb | identity |
| pine:mean_delta_ccc | 0.1410877942940506 | S22: data row 6 / mean_delta_ccc | identity |
| pine:n_units | 10 | S22: data row 6 / n_units | identity |
| pine:protocol | v13o O | S22: data row 6 / protocol | identity |
| pine:delta_ln_ccc | 0.21503441198089 | derived:pine:mean_delta_ln_pcc ; derived:pine:mean_delta_ln_cb | sum |
| rice:mean_delta_ln_pcc | 0.0231601061324773 | S22: data row 7 / mean_delta_ln_pcc | identity |
| rice:mean_delta_ln_cb | 0.0867822766222095 | S22: data row 7 / mean_delta_ln_cb | identity |
| rice:mean_delta_ccc | 0.0701793393838756 | S22: data row 7 / mean_delta_ccc | identity |
| rice:n_units | 10 | S22: data row 7 / n_units | identity |
| rice:protocol | v13o O | S22: data row 7 / protocol | identity |
| rice:delta_ln_ccc | 0.10994238275468679 | derived:rice:mean_delta_ln_pcc ; derived:rice:mean_delta_ln_cb | sum |
| wheatG:mean_delta_ln_pcc | 0.0227784378678625 | S22: data row 8 / mean_delta_ln_pcc | identity |
| wheatG:mean_delta_ln_cb | 0.372716263337402 | S22: data row 8 / mean_delta_ln_cb | identity |
| wheatG:mean_delta_ccc | 0.1645940835047338 | S22: data row 8 / mean_delta_ccc | identity |
| wheatG:n_units | 10 | S22: data row 8 / n_units | identity |
| wheatG:protocol | v13o O | S22: data row 8 / protocol | identity |
| wheatG:delta_ln_ccc | 0.3954947012052645 | derived:wheatG:mean_delta_ln_pcc ; derived:wheatG:mean_delta_ln_cb | sum |

### Fig. 4

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| sample:0.25:ratio | 0.25 | S13: data row 1 / ratio | identity |
| sample:0.25:AF | 0.4919989529514716 | S13: data row 1 / AF_mean_CCC | identity |
| sample:0.25:ranking | AF:0.491998953 > MLP-Dual:0.361631748 > Ridge:0.342010807 > SVR-RBF:0.321671169 > BayesB:0.294473676 > RF:0.269928707 > GBLUP:0.228942062 > VMGP:0.043556090 | S13: data row 1 / full_ranking | identity |
| sample:0.25:Ridge | 0.342010807 | derived:sample:0.25:ranking | ranking_value {"rank": 2} |
| sample:0.25:ranking | AF:0.491998953 > MLP-Dual:0.361631748 > Ridge:0.342010807 > SVR-RBF:0.321671169 > BayesB:0.294473676 > RF:0.269928707 > GBLUP:0.228942062 > VMGP:0.043556090 | S13: data row 1 / full_ranking | identity |
| sample:0.25:MLP-Dual | 0.361631748 | derived:sample:0.25:ranking | ranking_value {"rank": 1} |
| sample:0.5:ratio | 0.5 | S13: data row 2 / ratio | identity |
| sample:0.5:AF | 0.4865021119372883 | S13: data row 2 / AF_mean_CCC | identity |
| sample:0.5:ranking | AF:0.486502112 > MLP-Dual:0.433289145 > Ridge:0.410095249 > BayesB:0.399567037 > GBLUP:0.365194622 > SVR-RBF:0.348356741 > RF:0.272499688 > VMGP:0.106468305 | S13: data row 2 / full_ranking | identity |
| sample:0.5:Ridge | 0.410095249 | derived:sample:0.5:ranking | ranking_value {"rank": 2} |
| sample:0.5:ranking | AF:0.486502112 > MLP-Dual:0.433289145 > Ridge:0.410095249 > BayesB:0.399567037 > GBLUP:0.365194622 > SVR-RBF:0.348356741 > RF:0.272499688 > VMGP:0.106468305 | S13: data row 2 / full_ranking | identity |
| sample:0.5:MLP-Dual | 0.433289145 | derived:sample:0.5:ranking | ranking_value {"rank": 1} |
| sample:0.75:ratio | 0.75 | S13: data row 3 / ratio | identity |
| sample:0.75:AF | 0.558496935062656 | S13: data row 3 / AF_mean_CCC | identity |
| sample:0.75:ranking | AF:0.558496935 > MLP-Dual:0.462249123 > BayesB:0.457157868 > Ridge:0.453982822 > GBLUP:0.447475989 > SVR-RBF:0.425666751 > RF:0.369614219 > VMGP:0.163987449 | S13: data row 3 / full_ranking | identity |
| sample:0.75:Ridge | 0.453982822 | derived:sample:0.75:ranking | ranking_value {"rank": 3} |
| sample:0.75:ranking | AF:0.558496935 > MLP-Dual:0.462249123 > BayesB:0.457157868 > Ridge:0.453982822 > GBLUP:0.447475989 > SVR-RBF:0.425666751 > RF:0.369614219 > VMGP:0.163987449 | S13: data row 3 / full_ranking | identity |
| sample:0.75:MLP-Dual | 0.462249123 | derived:sample:0.75:ranking | ranking_value {"rank": 1} |
| sample:1.0:ratio | 1.0 | S13: data row 4 / ratio | identity |
| sample:1.0:AF | 0.591276726939898 | S13: data row 4 / AF_mean_CCC | identity |
| sample:1.0:ranking | AF:0.591276727 > BayesB:0.503297597 > Ridge:0.495941309 > GBLUP:0.473465787 > SVR-RBF:0.472798383 > MLP-Dual:0.422740111 > RF:0.402370318 > VMGP:0.130964600 | S13: data row 4 / full_ranking | identity |
| sample:1.0:Ridge | 0.495941309 | derived:sample:1.0:ranking | ranking_value {"rank": 2} |
| sample:1.0:ranking | AF:0.591276727 > BayesB:0.503297597 > Ridge:0.495941309 > GBLUP:0.473465787 > SVR-RBF:0.472798383 > MLP-Dual:0.422740111 > RF:0.402370318 > VMGP:0.130964600 | S13: data row 4 / full_ranking | identity |
| sample:1.0:MLP-Dual | 0.422740111 | derived:sample:1.0:ranking | ranking_value {"rank": 5} |
| marker:0.125:ratio | 0.125 | S13: data row 5 / ratio | identity |
| marker:0.125:AF | 0.5725695169724505 | S13: data row 5 / AF_mean_CCC | identity |
| marker:0.125:BayesB | 0.4835470977446605 | S13: data row 5 / corrected_BayesB_mean_CCC | identity |
| marker:0.125:ranking | AF:0.572569517 > Ridge:0.487072204 > BayesB:0.483547098 > GBLUP:0.467355101 > MLP-Dual:0.464172385 > SVR-RBF:0.456330213 > RF:0.404918243 > VMGP:0.176281149 | S13: data row 5 / full_ranking | identity |
| marker:0.125:Ridge | 0.487072204 | derived:marker:0.125:ranking | ranking_value {"rank": 1} |
| marker:0.25:ratio | 0.25 | S13: data row 6 / ratio | identity |
| marker:0.25:AF | 0.5740440079823156 | S13: data row 6 / AF_mean_CCC | identity |
| marker:0.25:BayesB | 0.5194265938043469 | S13: data row 6 / corrected_BayesB_mean_CCC | identity |
| marker:0.25:ranking | AF:0.574044008 > BayesB:0.519426594 > Ridge:0.503283920 > MLP-Dual:0.481174093 > GBLUP:0.474854452 > SVR-RBF:0.460798524 > RF:0.390432874 > VMGP:0.149598827 | S13: data row 6 / full_ranking | identity |
| marker:0.25:Ridge | 0.50328392 | derived:marker:0.25:ranking | ranking_value {"rank": 2} |
| marker:0.5:ratio | 0.5 | S13: data row 7 / ratio | identity |
| marker:0.5:AF | 0.5615502957269269 | S13: data row 7 / AF_mean_CCC | identity |
| marker:0.5:BayesB | 0.5116139326733482 | S13: data row 7 / corrected_BayesB_mean_CCC | identity |
| marker:0.5:ranking | AF:0.561550296 > SVR-RBF:0.511771307 > BayesB:0.511613933 > MLP-Dual:0.503034156 > Ridge:0.502154174 > GBLUP:0.496791470 > RF:0.421826683 > VMGP:0.182184153 | S13: data row 7 / full_ranking | identity |
| marker:0.5:Ridge | 0.502154174 | derived:marker:0.5:ranking | ranking_value {"rank": 4} |
| marker:shared100:ratio | 1.0 | S13: data row 4 / ratio | identity |
| marker:shared100:AF | 0.591276726939898 | S13: data row 4 / AF_mean_CCC | identity |
| marker:shared100:BayesB | 0.5032975969925397 | S13: data row 4 / corrected_BayesB_mean_CCC | identity |
| marker:shared100:ranking | AF:0.591276727 > BayesB:0.503297597 > Ridge:0.495941309 > GBLUP:0.473465787 > SVR-RBF:0.472798383 > MLP-Dual:0.422740111 > RF:0.402370318 > VMGP:0.130964600 | S13: data row 4 / full_ranking | identity |
| marker:shared100:Ridge | 0.495941309 | derived:marker:shared100:ranking | ranking_value {"rank": 2} |
| missing:AUS2015:AF:0.0:row1:baseline | 0.8135225802044967 | S25: data row 1 / ccc_population | identity |
| missing:AUS2015:AF:0.0:row1:observed | 0.8135225802044967 | S25: data row 1 / ccc_population | identity |
| missing:AUS2015:AF:0.0:row1:drop | 0.0 | derived:missing:AUS2015:AF:0.0:row1:baseline ; derived:missing:AUS2015:AF:0.0:row1:observed | subtract |
| missing:AUS2015:AF:0.0:row2:baseline | 0.8135225802044967 | S25: data row 2 / ccc_population | identity |
| missing:AUS2015:AF:0.0:row2:observed | 0.8135225802044967 | S25: data row 2 / ccc_population | identity |
| missing:AUS2015:AF:0.0:row2:drop | 0.0 | derived:missing:AUS2015:AF:0.0:row2:baseline ; derived:missing:AUS2015:AF:0.0:row2:observed | subtract |
| missing:AUS2015:AF:0.0:row3:baseline | 0.8135225802044967 | S25: data row 3 / ccc_population | identity |
| missing:AUS2015:AF:0.0:row3:observed | 0.8135225802044967 | S25: data row 3 / ccc_population | identity |
| missing:AUS2015:AF:0.0:row3:drop | 0.0 | derived:missing:AUS2015:AF:0.0:row3:baseline ; derived:missing:AUS2015:AF:0.0:row3:observed | subtract |
| missing:AUS2015:AF:0.0:mean_drop | 0.0 | derived:missing:AUS2015:AF:0.0:row1:drop ; derived:missing:AUS2015:AF:0.0:row2:drop ; derived:missing:AUS2015:AF:0.0:row3:drop | mean |
| missing:AUS2015:AF:0.0:units | 3 | derived:missing:AUS2015:AF:0.0:row1:drop ; derived:missing:AUS2015:AF:0.0:row2:drop ; derived:missing:AUS2015:AF:0.0:row3:drop | count |
| missing:AUS2015:AF:0.1:row7:baseline | 0.8135225802044967 | S25: data row 1 / ccc_population | identity |
| missing:AUS2015:AF:0.1:row7:observed | 0.8114340021257397 | S25: data row 7 / ccc_population | identity |
| missing:AUS2015:AF:0.1:row7:drop | 0.002088578078757064 | derived:missing:AUS2015:AF:0.1:row7:baseline ; derived:missing:AUS2015:AF:0.1:row7:observed | subtract |
| missing:AUS2015:AF:0.1:row8:baseline | 0.8135225802044967 | S25: data row 2 / ccc_population | identity |
| missing:AUS2015:AF:0.1:row8:observed | 0.8145726608126177 | S25: data row 8 / ccc_population | identity |
| missing:AUS2015:AF:0.1:row8:drop | -0.0010500806081209513 | derived:missing:AUS2015:AF:0.1:row8:baseline ; derived:missing:AUS2015:AF:0.1:row8:observed | subtract |
| missing:AUS2015:AF:0.1:row9:baseline | 0.8135225802044967 | S25: data row 3 / ccc_population | identity |
| missing:AUS2015:AF:0.1:row9:observed | 0.8136929862798691 | S25: data row 9 / ccc_population | identity |
| missing:AUS2015:AF:0.1:row9:drop | -0.00017040607537233132 | derived:missing:AUS2015:AF:0.1:row9:baseline ; derived:missing:AUS2015:AF:0.1:row9:observed | subtract |
| missing:AUS2015:AF:0.1:mean_drop | 0.0002893637984212605 | derived:missing:AUS2015:AF:0.1:row7:drop ; derived:missing:AUS2015:AF:0.1:row8:drop ; derived:missing:AUS2015:AF:0.1:row9:drop | mean |
| missing:AUS2015:AF:0.1:units | 3 | derived:missing:AUS2015:AF:0.1:row7:drop ; derived:missing:AUS2015:AF:0.1:row8:drop ; derived:missing:AUS2015:AF:0.1:row9:drop | count |
| missing:AUS2015:AF:0.5:row13:baseline | 0.8135225802044967 | S25: data row 1 / ccc_population | identity |
| missing:AUS2015:AF:0.5:row13:observed | 0.8053388063680753 | S25: data row 13 / ccc_population | identity |
| missing:AUS2015:AF:0.5:row13:drop | 0.008183773836421437 | derived:missing:AUS2015:AF:0.5:row13:baseline ; derived:missing:AUS2015:AF:0.5:row13:observed | subtract |
| missing:AUS2015:AF:0.5:row14:baseline | 0.8135225802044967 | S25: data row 2 / ccc_population | identity |
| missing:AUS2015:AF:0.5:row14:observed | 0.8135861341182702 | S25: data row 14 / ccc_population | identity |
| missing:AUS2015:AF:0.5:row14:drop | -6.355391377343977e-05 | derived:missing:AUS2015:AF:0.5:row14:baseline ; derived:missing:AUS2015:AF:0.5:row14:observed | subtract |
| missing:AUS2015:AF:0.5:row15:baseline | 0.8135225802044967 | S25: data row 3 / ccc_population | identity |
| missing:AUS2015:AF:0.5:row15:observed | 0.8114436189387633 | S25: data row 15 / ccc_population | identity |
| missing:AUS2015:AF:0.5:row15:drop | 0.002078961265733481 | derived:missing:AUS2015:AF:0.5:row15:baseline ; derived:missing:AUS2015:AF:0.5:row15:observed | subtract |
| missing:AUS2015:AF:0.5:mean_drop | 0.003399727062793826 | derived:missing:AUS2015:AF:0.5:row13:drop ; derived:missing:AUS2015:AF:0.5:row14:drop ; derived:missing:AUS2015:AF:0.5:row15:drop | mean |
| missing:AUS2015:AF:0.5:units | 3 | derived:missing:AUS2015:AF:0.5:row13:drop ; derived:missing:AUS2015:AF:0.5:row14:drop ; derived:missing:AUS2015:AF:0.5:row15:drop | count |
| missing:AUS2015:GBLUP:0.0:row1:drop | 0.0 | S24: data row 1 / delta_ccc_from_f0 | identity |
| missing:AUS2015:GBLUP:0.0:mean_drop | 0.0 | derived:missing:AUS2015:GBLUP:0.0:row1:drop | mean |
| missing:AUS2015:GBLUP:0.0:units | 1 | derived:missing:AUS2015:GBLUP:0.0:row1:drop | count |
| missing:AUS2015:GBLUP:0.1:row5:drop | 0.0247483950616135 | S24: data row 5 / delta_ccc_from_f0 | identity |
| missing:AUS2015:GBLUP:0.1:row6:drop | 0.0188671227509484 | S24: data row 6 / delta_ccc_from_f0 | identity |
| missing:AUS2015:GBLUP:0.1:row7:drop | 0.0233401785272305 | S24: data row 7 / delta_ccc_from_f0 | identity |
| missing:AUS2015:GBLUP:0.1:mean_drop | 0.022318565446597466 | derived:missing:AUS2015:GBLUP:0.1:row5:drop ; derived:missing:AUS2015:GBLUP:0.1:row6:drop ; derived:missing:AUS2015:GBLUP:0.1:row7:drop | mean |
| missing:AUS2015:GBLUP:0.1:units | 3 | derived:missing:AUS2015:GBLUP:0.1:row5:drop ; derived:missing:AUS2015:GBLUP:0.1:row6:drop ; derived:missing:AUS2015:GBLUP:0.1:row7:drop | count |
| missing:AUS2015:GBLUP:0.5:row11:drop | 0.2429327018941691 | S24: data row 11 / delta_ccc_from_f0 | identity |
| missing:AUS2015:GBLUP:0.5:row12:drop | 0.2282791844096769 | S24: data row 12 / delta_ccc_from_f0 | identity |
| missing:AUS2015:GBLUP:0.5:row13:drop | 0.2319112572043062 | S24: data row 13 / delta_ccc_from_f0 | identity |
| missing:AUS2015:GBLUP:0.5:mean_drop | 0.23437438116938406 | derived:missing:AUS2015:GBLUP:0.5:row11:drop ; derived:missing:AUS2015:GBLUP:0.5:row12:drop ; derived:missing:AUS2015:GBLUP:0.5:row13:drop | mean |
| missing:AUS2015:GBLUP:0.5:units | 3 | derived:missing:AUS2015:GBLUP:0.5:row11:drop ; derived:missing:AUS2015:GBLUP:0.5:row12:drop ; derived:missing:AUS2015:GBLUP:0.5:row13:drop | count |
| missing:GABI:AF:0.0:row61:drop | 2.435965562597175e-08 | S27: data row 61 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row62:drop | 2.435965562597175e-08 | S27: data row 62 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row63:drop | 2.435965562597175e-08 | S27: data row 63 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row73:drop | 2.023346379331769e-09 | S27: data row 73 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row74:drop | 2.023346379331769e-09 | S27: data row 74 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row75:drop | 2.023346379331769e-09 | S27: data row 75 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row85:drop | -1.2356365930443758e-08 | S27: data row 85 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row86:drop | -1.2356365930443758e-08 | S27: data row 86 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row87:drop | -1.2356365930443758e-08 | S27: data row 87 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row97:drop | -4.2950353384973994e-08 | S27: data row 97 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row98:drop | -4.2950353384973994e-08 | S27: data row 98 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row99:drop | -4.2950353384973994e-08 | S27: data row 99 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row109:drop | -1.0094494240497909e-08 | S27: data row 109 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row110:drop | -1.0094494240497909e-08 | S27: data row 110 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:row111:drop | -1.0094494240497909e-08 | S27: data row 111 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.0:mean_drop | -7.803642310122428e-09 | derived:missing:GABI:AF:0.0:row61:drop ; derived:missing:GABI:AF:0.0:row62:drop ; derived:missing:GABI:AF:0.0:row63:drop ; derived:missing:GABI:AF:0.0:row73:drop ; derived:missing:GABI:AF:0.0:row74:drop ; derived:missing:GABI:AF:0.0:row75:drop ; derived:missing:GABI:AF:0.0:row85:drop ; derived:missing:GABI:AF:0.0:row86:drop ; derived:missing:GABI:AF:0.0:row87:drop ; derived:missing:GABI:AF:0.0:row97:drop ; derived:missing:GABI:AF:0.0:row98:drop ; derived:missing:GABI:AF:0.0:row99:drop ; derived:missing:GABI:AF:0.0:row109:drop ; derived:missing:GABI:AF:0.0:row110:drop ; derived:missing:GABI:AF:0.0:row111:drop | mean |
| missing:GABI:AF:0.0:units | 15 | derived:missing:GABI:AF:0.0:row61:drop ; derived:missing:GABI:AF:0.0:row62:drop ; derived:missing:GABI:AF:0.0:row63:drop ; derived:missing:GABI:AF:0.0:row73:drop ; derived:missing:GABI:AF:0.0:row74:drop ; derived:missing:GABI:AF:0.0:row75:drop ; derived:missing:GABI:AF:0.0:row85:drop ; derived:missing:GABI:AF:0.0:row86:drop ; derived:missing:GABI:AF:0.0:row87:drop ; derived:missing:GABI:AF:0.0:row97:drop ; derived:missing:GABI:AF:0.0:row98:drop ; derived:missing:GABI:AF:0.0:row99:drop ; derived:missing:GABI:AF:0.0:row109:drop ; derived:missing:GABI:AF:0.0:row110:drop ; derived:missing:GABI:AF:0.0:row111:drop | count |
| missing:GABI:AF:0.1:row64:drop | 0.0228093189833462 | S27: data row 64 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row65:drop | 0.0089161291146689 | S27: data row 65 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row66:drop | 0.0007127888453239 | S27: data row 66 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row76:drop | 0.0234384074653398 | S27: data row 76 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row77:drop | 0.0045961144436839 | S27: data row 77 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row78:drop | -0.0023436693962313 | S27: data row 78 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row88:drop | 0.0163992489489525 | S27: data row 88 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row89:drop | 0.0026919153055872 | S27: data row 89 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row90:drop | -0.0038461749023183 | S27: data row 90 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row100:drop | 0.0147199861989922 | S27: data row 100 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row101:drop | -0.0016689393224855 | S27: data row 101 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row102:drop | -0.0068239419643103 | S27: data row 102 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row112:drop | 0.0149505104992793 | S27: data row 112 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row113:drop | 0.0024603349866633 | S27: data row 113 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:row114:drop | -0.0054186247493096 | S27: data row 114 / ccc_drop_from_f0 | identity |
| missing:GABI:AF:0.1:mean_drop | 0.0061062269638121475 | derived:missing:GABI:AF:0.1:row64:drop ; derived:missing:GABI:AF:0.1:row65:drop ; derived:missing:GABI:AF:0.1:row66:drop ; derived:missing:GABI:AF:0.1:row76:drop ; derived:missing:GABI:AF:0.1:row77:drop ; derived:missing:GABI:AF:0.1:row78:drop ; derived:missing:GABI:AF:0.1:row88:drop ; derived:missing:GABI:AF:0.1:row89:drop ; derived:missing:GABI:AF:0.1:row90:drop ; derived:missing:GABI:AF:0.1:row100:drop ; derived:missing:GABI:AF:0.1:row101:drop ; derived:missing:GABI:AF:0.1:row102:drop ; derived:missing:GABI:AF:0.1:row112:drop ; derived:missing:GABI:AF:0.1:row113:drop ; derived:missing:GABI:AF:0.1:row114:drop | mean |
| missing:GABI:AF:0.1:units | 15 | derived:missing:GABI:AF:0.1:row64:drop ; derived:missing:GABI:AF:0.1:row65:drop ; derived:missing:GABI:AF:0.1:row66:drop ; derived:missing:GABI:AF:0.1:row76:drop ; derived:missing:GABI:AF:0.1:row77:drop ; derived:missing:GABI:AF:0.1:row78:drop ; derived:missing:GABI:AF:0.1:row88:drop ; derived:missing:GABI:AF:0.1:row89:drop ; derived:missing:GABI:AF:0.1:row90:drop ; derived:missing:GABI:AF:0.1:row100:drop ; derived:missing:GABI:AF:0.1:row101:drop ; derived:missing:GABI:AF:0.1:row102:drop ; derived:missing:GABI:AF:0.1:row112:drop ; derived:missing:GABI:AF:0.1:row113:drop ; derived:missing:GABI:AF:0.1:row114:drop | count |
| missing:Ward:AF:0.0:row1:drop | 2.694181544526941e-09 | S27: data row 1 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row2:drop | 2.694181544526941e-09 | S27: data row 2 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row3:drop | 2.694181544526941e-09 | S27: data row 3 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row13:drop | 1.2609321808909613e-08 | S27: data row 13 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row14:drop | 1.2609321808909613e-08 | S27: data row 14 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row15:drop | 1.2609321808909613e-08 | S27: data row 15 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row25:drop | 2.702331358683807e-08 | S27: data row 25 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row26:drop | 2.702331358683807e-08 | S27: data row 26 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row27:drop | 2.702331358683807e-08 | S27: data row 27 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row37:drop | 9.338844308981464e-09 | S27: data row 37 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row38:drop | 9.338844308981464e-09 | S27: data row 38 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row39:drop | 9.338844308981464e-09 | S27: data row 39 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row49:drop | 5.511819611836444e-09 | S27: data row 49 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row50:drop | 5.511819611836444e-09 | S27: data row 50 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:row51:drop | 5.511819611836444e-09 | S27: data row 51 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.0:mean_drop | 1.1435496172218506e-08 | derived:missing:Ward:AF:0.0:row1:drop ; derived:missing:Ward:AF:0.0:row2:drop ; derived:missing:Ward:AF:0.0:row3:drop ; derived:missing:Ward:AF:0.0:row13:drop ; derived:missing:Ward:AF:0.0:row14:drop ; derived:missing:Ward:AF:0.0:row15:drop ; derived:missing:Ward:AF:0.0:row25:drop ; derived:missing:Ward:AF:0.0:row26:drop ; derived:missing:Ward:AF:0.0:row27:drop ; derived:missing:Ward:AF:0.0:row37:drop ; derived:missing:Ward:AF:0.0:row38:drop ; derived:missing:Ward:AF:0.0:row39:drop ; derived:missing:Ward:AF:0.0:row49:drop ; derived:missing:Ward:AF:0.0:row50:drop ; derived:missing:Ward:AF:0.0:row51:drop | mean |
| missing:Ward:AF:0.0:units | 15 | derived:missing:Ward:AF:0.0:row1:drop ; derived:missing:Ward:AF:0.0:row2:drop ; derived:missing:Ward:AF:0.0:row3:drop ; derived:missing:Ward:AF:0.0:row13:drop ; derived:missing:Ward:AF:0.0:row14:drop ; derived:missing:Ward:AF:0.0:row15:drop ; derived:missing:Ward:AF:0.0:row25:drop ; derived:missing:Ward:AF:0.0:row26:drop ; derived:missing:Ward:AF:0.0:row27:drop ; derived:missing:Ward:AF:0.0:row37:drop ; derived:missing:Ward:AF:0.0:row38:drop ; derived:missing:Ward:AF:0.0:row39:drop ; derived:missing:Ward:AF:0.0:row49:drop ; derived:missing:Ward:AF:0.0:row50:drop ; derived:missing:Ward:AF:0.0:row51:drop | count |
| missing:Ward:AF:0.1:row4:drop | 0.0163067885733519 | S27: data row 4 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row5:drop | 0.0041337486743612 | S27: data row 5 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row6:drop | 0.0082427720615291 | S27: data row 6 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row16:drop | 0.0178497750390602 | S27: data row 16 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row17:drop | 0.0031896933194108 | S27: data row 17 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row18:drop | 0.0079884360188976 | S27: data row 18 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row28:drop | 0.0161454438253571 | S27: data row 28 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row29:drop | 0.0026483991853367 | S27: data row 29 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row30:drop | 0.0081460544216824 | S27: data row 30 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row40:drop | 0.016820741974016 | S27: data row 40 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row41:drop | 0.003371023042922 | S27: data row 41 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row42:drop | 0.0074516785215045 | S27: data row 42 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row52:drop | 0.0143516179460732 | S27: data row 52 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row53:drop | 0.0025232235042431 | S27: data row 53 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:row54:drop | 0.0064093552104906 | S27: data row 54 / ccc_drop_from_f0 | identity |
| missing:Ward:AF:0.1:mean_drop | 0.009038583421215761 | derived:missing:Ward:AF:0.1:row4:drop ; derived:missing:Ward:AF:0.1:row5:drop ; derived:missing:Ward:AF:0.1:row6:drop ; derived:missing:Ward:AF:0.1:row16:drop ; derived:missing:Ward:AF:0.1:row17:drop ; derived:missing:Ward:AF:0.1:row18:drop ; derived:missing:Ward:AF:0.1:row28:drop ; derived:missing:Ward:AF:0.1:row29:drop ; derived:missing:Ward:AF:0.1:row30:drop ; derived:missing:Ward:AF:0.1:row40:drop ; derived:missing:Ward:AF:0.1:row41:drop ; derived:missing:Ward:AF:0.1:row42:drop ; derived:missing:Ward:AF:0.1:row52:drop ; derived:missing:Ward:AF:0.1:row53:drop ; derived:missing:Ward:AF:0.1:row54:drop | mean |
| missing:Ward:AF:0.1:units | 15 | derived:missing:Ward:AF:0.1:row4:drop ; derived:missing:Ward:AF:0.1:row5:drop ; derived:missing:Ward:AF:0.1:row6:drop ; derived:missing:Ward:AF:0.1:row16:drop ; derived:missing:Ward:AF:0.1:row17:drop ; derived:missing:Ward:AF:0.1:row18:drop ; derived:missing:Ward:AF:0.1:row28:drop ; derived:missing:Ward:AF:0.1:row29:drop ; derived:missing:Ward:AF:0.1:row30:drop ; derived:missing:Ward:AF:0.1:row40:drop ; derived:missing:Ward:AF:0.1:row41:drop ; derived:missing:Ward:AF:0.1:row42:drop ; derived:missing:Ward:AF:0.1:row52:drop ; derived:missing:Ward:AF:0.1:row53:drop ; derived:missing:Ward:AF:0.1:row54:drop | count |
| missing:GABI:GBLUP:0.0:row1:drop | 0.0 | S26: data row 1 / ccc_drop_from_f0 | identity |
| missing:GABI:GBLUP:0.0:row2:drop | 0.0 | S26: data row 2 / ccc_drop_from_f0 | identity |
| missing:GABI:GBLUP:0.0:row3:drop | 0.0 | S26: data row 3 / ccc_drop_from_f0 | identity |
| missing:GABI:GBLUP:0.0:mean_drop | 0.0 | derived:missing:GABI:GBLUP:0.0:row1:drop ; derived:missing:GABI:GBLUP:0.0:row2:drop ; derived:missing:GABI:GBLUP:0.0:row3:drop | mean |
| missing:GABI:GBLUP:0.0:units | 3 | derived:missing:GABI:GBLUP:0.0:row1:drop ; derived:missing:GABI:GBLUP:0.0:row2:drop ; derived:missing:GABI:GBLUP:0.0:row3:drop | count |
| missing:GABI:GBLUP:0.1:row4:drop | 0.0225200355629404 | S26: data row 4 / ccc_drop_from_f0 | identity |
| missing:GABI:GBLUP:0.1:row5:drop | 0.0145786720460237 | S26: data row 5 / ccc_drop_from_f0 | identity |
| missing:GABI:GBLUP:0.1:row6:drop | 0.0301820327747119 | S26: data row 6 / ccc_drop_from_f0 | identity |
| missing:GABI:GBLUP:0.1:mean_drop | 0.022426913461225332 | derived:missing:GABI:GBLUP:0.1:row4:drop ; derived:missing:GABI:GBLUP:0.1:row5:drop ; derived:missing:GABI:GBLUP:0.1:row6:drop | mean |
| missing:GABI:GBLUP:0.1:units | 3 | derived:missing:GABI:GBLUP:0.1:row4:drop ; derived:missing:GABI:GBLUP:0.1:row5:drop ; derived:missing:GABI:GBLUP:0.1:row6:drop | count |
| missing:Ward:GBLUP:0.0:row13:drop | 0.0 | S26: data row 13 / ccc_drop_from_f0 | identity |
| missing:Ward:GBLUP:0.0:row14:drop | 0.0 | S26: data row 14 / ccc_drop_from_f0 | identity |
| missing:Ward:GBLUP:0.0:row15:drop | 0.0 | S26: data row 15 / ccc_drop_from_f0 | identity |
| missing:Ward:GBLUP:0.0:mean_drop | 0.0 | derived:missing:Ward:GBLUP:0.0:row13:drop ; derived:missing:Ward:GBLUP:0.0:row14:drop ; derived:missing:Ward:GBLUP:0.0:row15:drop | mean |
| missing:Ward:GBLUP:0.0:units | 3 | derived:missing:Ward:GBLUP:0.0:row13:drop ; derived:missing:Ward:GBLUP:0.0:row14:drop ; derived:missing:Ward:GBLUP:0.0:row15:drop | count |
| missing:Ward:GBLUP:0.1:row16:drop | 0.0214126490353895 | S26: data row 16 / ccc_drop_from_f0 | identity |
| missing:Ward:GBLUP:0.1:row17:drop | 0.0171532498255551 | S26: data row 17 / ccc_drop_from_f0 | identity |
| missing:Ward:GBLUP:0.1:row18:drop | 0.0255870554829317 | S26: data row 18 / ccc_drop_from_f0 | identity |
| missing:Ward:GBLUP:0.1:mean_drop | 0.021384318114625434 | derived:missing:Ward:GBLUP:0.1:row16:drop ; derived:missing:Ward:GBLUP:0.1:row17:drop ; derived:missing:Ward:GBLUP:0.1:row18:drop | mean |
| missing:Ward:GBLUP:0.1:units | 3 | derived:missing:Ward:GBLUP:0.1:row16:drop ; derived:missing:Ward:GBLUP:0.1:row17:drop ; derived:missing:Ward:GBLUP:0.1:row18:drop | count |
| applicability:AUS2015:Cb | 0.9625807858515576 | S19: data row 1 / linear_cb | identity |
| applicability:AUS2015:delta | -0.0588643092003607 | S19: data row 1 / af_minus_linear_ccc | identity |
| applicability:GABI:Cb | 0.9090750821214816 | S19: data row 4 / linear_cb | identity |
| applicability:GABI:delta | 0.0008045227659936 | S19: data row 4 / af_minus_linear_ccc | identity |
| applicability:Ward:Cb | 0.6842865868332173 | S19: data row 7 / linear_cb | identity |
| applicability:Ward:delta | 0.0977235194814853 | S19: data row 7 / af_minus_linear_ccc | identity |
| applicability:lentil:Cb | 0.9781753026854572 | S19: data row 19 / linear_cb | identity |
| applicability:lentil:delta | -0.0347240154363384 | S19: data row 19 / af_minus_linear_ccc | identity |
| applicability:pine:Cb | 0.9631606259765308 | S19: data row 22 / linear_cb | identity |
| applicability:pine:delta | -0.0022866891874421 | S19: data row 22 / af_minus_linear_ccc | identity |
| applicability:rice:Cb | 0.9517057139635678 | S19: data row 13 / linear_cb | identity |
| applicability:rice:delta | 0.0200833431876276 | S19: data row 13 / af_minus_linear_ccc | identity |
| applicability:wheatG:Cb | 0.9118641085018796 | S19: data row 10 / linear_cb | identity |
| applicability:wheatG:delta | -0.020836833640794 | S19: data row 10 / af_minus_linear_ccc | identity |
| applicability:Spearman_rho | -0.6785714285714287 | derived:applicability:AUS2015:Cb ; derived:applicability:GABI:Cb ; derived:applicability:Ward:Cb ; derived:applicability:lentil:Cb ; derived:applicability:pine:Cb ; derived:applicability:rice:Cb ; derived:applicability:wheatG:Cb ; derived:applicability:AUS2015:delta ; derived:applicability:GABI:delta ; derived:applicability:Ward:delta ; derived:applicability:lentil:delta ; derived:applicability:pine:delta ; derived:applicability:rice:delta ; derived:applicability:wheatG:delta | spearman |
| applicability:n | 7 | derived:applicability:AUS2015:Cb ; derived:applicability:GABI:Cb ; derived:applicability:Ward:Cb ; derived:applicability:lentil:Cb ; derived:applicability:pine:Cb ; derived:applicability:rice:Cb ; derived:applicability:wheatG:Cb | count |

### Fig. 5

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| seven_dataset_decisions:passed | 28 | S11: data row 1 / passes_original_D_rule ; S11: data row 2 / passes_original_D_rule ; S11: data row 3 / passes_original_D_rule ; S11: data row 4 / passes_original_D_rule ; S11: data row 5 / passes_original_D_rule ; S11: data row 6 / passes_original_D_rule ; S11: data row 7 / passes_original_D_rule ; S11: data row 8 / passes_original_D_rule ; S11: data row 9 / passes_original_D_rule ; S11: data row 10 / passes_original_D_rule ; S11: data row 11 / passes_original_D_rule ; S11: data row 12 / passes_original_D_rule ; S11: data row 17 / passes_original_D_rule ; S11: data row 18 / passes_original_D_rule ; S11: data row 19 / passes_original_D_rule ; S11: data row 20 / passes_original_D_rule ; S11: data row 21 / passes_original_D_rule ; S11: data row 22 / passes_original_D_rule ; S11: data row 23 / passes_original_D_rule ; S11: data row 24 / passes_original_D_rule ; S11: data row 25 / passes_original_D_rule ; S11: data row 26 / passes_original_D_rule ; S11: data row 27 / passes_original_D_rule ; S11: data row 28 / passes_original_D_rule ; S11: data row 29 / passes_original_D_rule ; S11: data row 30 / passes_original_D_rule ; S11: data row 31 / passes_original_D_rule ; S11: data row 32 / passes_original_D_rule | count_equal {"target": true} |
| seven_dataset_decisions:total | 28 | S11: data row 1 / metric ; S11: data row 2 / metric ; S11: data row 3 / metric ; S11: data row 4 / metric ; S11: data row 5 / metric ; S11: data row 6 / metric ; S11: data row 7 / metric ; S11: data row 8 / metric ; S11: data row 9 / metric ; S11: data row 10 / metric ; S11: data row 11 / metric ; S11: data row 12 / metric ; S11: data row 17 / metric ; S11: data row 18 / metric ; S11: data row 19 / metric ; S11: data row 20 / metric ; S11: data row 21 / metric ; S11: data row 22 / metric ; S11: data row 23 / metric ; S11: data row 24 / metric ; S11: data row 25 / metric ; S11: data row 26 / metric ; S11: data row 27 / metric ; S11: data row 28 / metric ; S11: data row 29 / metric ; S11: data row 30 / metric ; S11: data row 31 / metric ; S11: data row 32 / metric | count |
| inflation:AUS2015:AF-MT:pcc | 0.0953526918668735 | S11: data row 1 / mean | identity |
| inflation:AUS2015:AF-MT:pcc:positive | True | S11: data row 1 / passes_original_D_rule | identity |
| inflation:GABI:AF-MT:pcc | 0.2624855790407826 | S11: data row 5 / mean | identity |
| inflation:GABI:AF-MT:pcc:positive | True | S11: data row 5 / passes_original_D_rule | identity |
| inflation:Ward:AF-MT:pcc | 0.549657084744928 | S11: data row 9 / mean | identity |
| inflation:Ward:AF-MT:pcc:positive | True | S11: data row 9 / passes_original_D_rule | identity |
| inflation:lentil:AF-MT:pcc | 0.1409767105130817 | S11: data row 17 / mean | identity |
| inflation:lentil:AF-MT:pcc:positive | True | S11: data row 17 / passes_original_D_rule | identity |
| inflation:pine:AF-MT:pcc | 0.0980165549409106 | S11: data row 21 / mean | identity |
| inflation:pine:AF-MT:pcc:positive | True | S11: data row 21 / passes_original_D_rule | identity |
| inflation:rice:AF-MT:pcc | 0.2090403923257409 | S11: data row 25 / mean | identity |
| inflation:rice:AF-MT:pcc:positive | True | S11: data row 25 / passes_original_D_rule | identity |
| inflation:wheatG:AF-MT:pcc | 0.333749842803539 | S11: data row 29 / mean | identity |
| inflation:wheatG:AF-MT:pcc:positive | True | S11: data row 29 / passes_original_D_rule | identity |
| inflation:AUS2015:AF-MT:ccc_population | 0.0777251032835816 | S11: data row 2 / mean | identity |
| inflation:AUS2015:AF-MT:ccc_population:positive | True | S11: data row 2 / passes_original_D_rule | identity |
| inflation:GABI:AF-MT:ccc_population | 0.2707276543547462 | S11: data row 6 / mean | identity |
| inflation:GABI:AF-MT:ccc_population:positive | True | S11: data row 6 / passes_original_D_rule | identity |
| inflation:Ward:AF-MT:ccc_population | 0.5447514406788913 | S11: data row 10 / mean | identity |
| inflation:Ward:AF-MT:ccc_population:positive | True | S11: data row 10 / passes_original_D_rule | identity |
| inflation:lentil:AF-MT:ccc_population | 0.1661553097932032 | S11: data row 18 / mean | identity |
| inflation:lentil:AF-MT:ccc_population:positive | True | S11: data row 18 / passes_original_D_rule | identity |
| inflation:pine:AF-MT:ccc_population | 0.0962701791825649 | S11: data row 22 / mean | identity |
| inflation:pine:AF-MT:ccc_population:positive | True | S11: data row 22 / passes_original_D_rule | identity |
| inflation:rice:AF-MT:ccc_population | 0.2081853438311691 | S11: data row 26 / mean | identity |
| inflation:rice:AF-MT:ccc_population:positive | True | S11: data row 26 / passes_original_D_rule | identity |
| inflation:wheatG:AF-MT:ccc_population | 0.3687981687704996 | S11: data row 30 / mean | identity |
| inflation:wheatG:AF-MT:ccc_population:positive | True | S11: data row 30 / passes_original_D_rule | identity |
| inflation:AUS2015:MLP-Dual:pcc | 0.1299546432506373 | S11: data row 3 / mean | identity |
| inflation:AUS2015:MLP-Dual:pcc:positive | True | S11: data row 3 / passes_original_D_rule | identity |
| inflation:GABI:MLP-Dual:pcc | 0.2722633200846618 | S11: data row 7 / mean | identity |
| inflation:GABI:MLP-Dual:pcc:positive | True | S11: data row 7 / passes_original_D_rule | identity |
| inflation:Ward:MLP-Dual:pcc | 0.5632916859129165 | S11: data row 11 / mean | identity |
| inflation:Ward:MLP-Dual:pcc:positive | True | S11: data row 11 / passes_original_D_rule | identity |
| inflation:lentil:MLP-Dual:pcc | 0.1267434444625242 | S11: data row 19 / mean | identity |
| inflation:lentil:MLP-Dual:pcc:positive | True | S11: data row 19 / passes_original_D_rule | identity |
| inflation:pine:MLP-Dual:pcc | 0.1257124414802048 | S11: data row 23 / mean | identity |
| inflation:pine:MLP-Dual:pcc:positive | True | S11: data row 23 / passes_original_D_rule | identity |
| inflation:rice:MLP-Dual:pcc | 0.1981275840375506 | S11: data row 27 / mean | identity |
| inflation:rice:MLP-Dual:pcc:positive | True | S11: data row 27 / passes_original_D_rule | identity |
| inflation:wheatG:MLP-Dual:pcc | 0.2778146359180533 | S11: data row 31 / mean | identity |
| inflation:wheatG:MLP-Dual:pcc:positive | True | S11: data row 31 / passes_original_D_rule | identity |
| inflation:AUS2015:MLP-Dual:ccc_population | 0.0914696525581298 | S11: data row 4 / mean | identity |
| inflation:AUS2015:MLP-Dual:ccc_population:positive | True | S11: data row 4 / passes_original_D_rule | identity |
| inflation:GABI:MLP-Dual:ccc_population | 0.3106212663406681 | S11: data row 8 / mean | identity |
| inflation:GABI:MLP-Dual:ccc_population:positive | True | S11: data row 8 / passes_original_D_rule | identity |
| inflation:Ward:MLP-Dual:ccc_population | 0.613756853524116 | S11: data row 12 / mean | identity |
| inflation:Ward:MLP-Dual:ccc_population:positive | True | S11: data row 12 / passes_original_D_rule | identity |
| inflation:lentil:MLP-Dual:ccc_population | 0.1143265586810861 | S11: data row 20 / mean | identity |
| inflation:lentil:MLP-Dual:ccc_population:positive | True | S11: data row 20 / passes_original_D_rule | identity |
| inflation:pine:MLP-Dual:ccc_population | 0.1326335391147043 | S11: data row 24 / mean | identity |
| inflation:pine:MLP-Dual:ccc_population:positive | True | S11: data row 24 / passes_original_D_rule | identity |
| inflation:rice:MLP-Dual:ccc_population | 0.202820289970338 | S11: data row 28 / mean | identity |
| inflation:rice:MLP-Dual:ccc_population:positive | True | S11: data row 28 / passes_original_D_rule | identity |
| inflation:wheatG:MLP-Dual:ccc_population | 0.3038981349305432 | S11: data row 32 / mean | identity |
| inflation:wheatG:MLP-Dual:ccc_population:positive | True | S11: data row 32 / passes_original_D_rule | identity |
| AUS2015:rank_scoped | 1.0 | S03: data row 9 / normative_rank | identity |
| AUS2015:rank_naive | 3.0 | S03: data row 9 / naive_rank | identity |
| GABI:rank_scoped | 2.0 | S03: data row 10 / normative_rank | identity |
| GABI:rank_naive | 2.0 | S03: data row 10 / naive_rank | identity |
| Ward:rank_scoped | 3.0 | S03: data row 11 / normative_rank | identity |
| Ward:rank_naive | 1.0 | S03: data row 11 / naive_rank | identity |
| false_lead:CCC:numerator | 6 | S17: data row 3 / without_bean_numerator | identity |
| false_lead:CCC:denominator | 7 | S17: data row 3 / without_bean_denominator | identity |
| false_lead:CCC:classic_check | 6 | S02: data row 1 / false_winner_dataset ; S02: data row 3 / false_winner_dataset ; S02: data row 5 / false_winner_dataset ; S02: data row 7 / false_winner_dataset ; S02: data row 9 / false_winner_dataset ; S02: data row 13 / false_winner_dataset ; S02: data row 15 / false_winner_dataset | count_equal {"target": true} |
| false_lead:PCC:numerator | 7 | S17: data row 4 / without_bean_numerator | identity |
| false_lead:PCC:denominator | 7 | S17: data row 4 / without_bean_denominator | identity |
| false_lead:PCC:classic_check | 7 | S02: data row 2 / false_winner_dataset ; S02: data row 4 / false_winner_dataset ; S02: data row 6 / false_winner_dataset ; S02: data row 8 / false_winner_dataset ; S02: data row 10 / false_winner_dataset ; S02: data row 14 / false_winner_dataset ; S02: data row 16 / false_winner_dataset | count_equal {"target": true} |

### Table V

| element | 源精度值 | 文件与定位 | 算式 |
| --- | --- | --- | --- |
| AUS2015:raw_markers | 23899 | S01: regex ^\\| AUS2015 \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 1 | identity |
| AUS2015:dimension:fold1 | 1004 | S01: regex ^\\| AUS2015 \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 2 | identity |
| AUS2015:dimension:fold1:compression | 23.80378486055777 | derived:AUS2015:raw_markers ; derived:AUS2015:dimension:fold1 | divide |
| AUS2015:dimension:fold2 | 1003 | S01: regex ^\\| AUS2015 \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 3 | identity |
| AUS2015:dimension:fold2:compression | 23.82751744765703 | derived:AUS2015:raw_markers ; derived:AUS2015:dimension:fold2 | divide |
| AUS2015:dimension:fold3 | 1003 | S01: regex ^\\| AUS2015 \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 4 | identity |
| AUS2015:dimension:fold3:compression | 23.82751744765703 | derived:AUS2015:raw_markers ; derived:AUS2015:dimension:fold3 | divide |
| AUS2015:dimension:fold4 | 1007 | S01: regex ^\\| AUS2015 \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 5 | identity |
| AUS2015:dimension:fold4:compression | 23.73286991062562 | derived:AUS2015:raw_markers ; derived:AUS2015:dimension:fold4 | divide |
| AUS2015:dimension:fold5 | 1005 | S01: regex ^\\| AUS2015 \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 6 | identity |
| AUS2015:dimension:fold5:compression | 23.780099502487563 | derived:AUS2015:raw_markers ; derived:AUS2015:dimension:fold5 | divide |
| AUS2015:dim_min | 1003 | derived:AUS2015:dimension:fold1 ; derived:AUS2015:dimension:fold2 ; derived:AUS2015:dimension:fold3 ; derived:AUS2015:dimension:fold4 ; derived:AUS2015:dimension:fold5 | min |
| AUS2015:dim_max | 1007 | derived:AUS2015:dimension:fold1 ; derived:AUS2015:dimension:fold2 ; derived:AUS2015:dimension:fold3 ; derived:AUS2015:dimension:fold4 ; derived:AUS2015:dimension:fold5 | max |
| AUS2015:compression_min | 23.73286991062562 | derived:AUS2015:dimension:fold1:compression ; derived:AUS2015:dimension:fold2:compression ; derived:AUS2015:dimension:fold3:compression ; derived:AUS2015:dimension:fold4:compression ; derived:AUS2015:dimension:fold5:compression | min |
| AUS2015:compression_max | 23.82751744765703 | derived:AUS2015:dimension:fold1:compression ; derived:AUS2015:dimension:fold2:compression ; derived:AUS2015:dimension:fold3:compression ; derived:AUS2015:dimension:fold4:compression ; derived:AUS2015:dimension:fold5:compression | max |
| GABI:raw_markers | 35143 | S01: regex ^\\| GABI \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 1 | identity |
| GABI:dimension:fold1 | 1004 | S01: regex ^\\| GABI \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 2 | identity |
| GABI:dimension:fold1:compression | 35.00298804780876 | derived:GABI:raw_markers ; derived:GABI:dimension:fold1 | divide |
| GABI:dimension:fold2 | 1008 | S01: regex ^\\| GABI \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 3 | identity |
| GABI:dimension:fold2:compression | 34.864087301587304 | derived:GABI:raw_markers ; derived:GABI:dimension:fold2 | divide |
| GABI:dimension:fold3 | 1005 | S01: regex ^\\| GABI \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 4 | identity |
| GABI:dimension:fold3:compression | 34.9681592039801 | derived:GABI:raw_markers ; derived:GABI:dimension:fold3 | divide |
| GABI:dimension:fold4 | 1008 | S01: regex ^\\| GABI \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 5 | identity |
| GABI:dimension:fold4:compression | 34.864087301587304 | derived:GABI:raw_markers ; derived:GABI:dimension:fold4 | divide |
| GABI:dimension:fold5 | 1004 | S01: regex ^\\| GABI \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 6 | identity |
| GABI:dimension:fold5:compression | 35.00298804780876 | derived:GABI:raw_markers ; derived:GABI:dimension:fold5 | divide |
| GABI:dim_min | 1004 | derived:GABI:dimension:fold1 ; derived:GABI:dimension:fold2 ; derived:GABI:dimension:fold3 ; derived:GABI:dimension:fold4 ; derived:GABI:dimension:fold5 | min |
| GABI:dim_max | 1008 | derived:GABI:dimension:fold1 ; derived:GABI:dimension:fold2 ; derived:GABI:dimension:fold3 ; derived:GABI:dimension:fold4 ; derived:GABI:dimension:fold5 | max |
| GABI:compression_min | 34.864087301587304 | derived:GABI:dimension:fold1:compression ; derived:GABI:dimension:fold2:compression ; derived:GABI:dimension:fold3:compression ; derived:GABI:dimension:fold4:compression ; derived:GABI:dimension:fold5:compression | min |
| GABI:compression_max | 35.00298804780876 | derived:GABI:dimension:fold1:compression ; derived:GABI:dimension:fold2:compression ; derived:GABI:dimension:fold3:compression ; derived:GABI:dimension:fold4:compression ; derived:GABI:dimension:fold5:compression | max |
| Ward:raw_markers | 29949 | S01: regex ^\\| Ward \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 1 | identity |
| Ward:dimension:fold1 | 1007 | S01: regex ^\\| Ward \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 2 | identity |
| Ward:dimension:fold1:compression | 29.740814299900695 | derived:Ward:raw_markers ; derived:Ward:dimension:fold1 | divide |
| Ward:dimension:fold2 | 1006 | S01: regex ^\\| Ward \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 3 | identity |
| Ward:dimension:fold2:compression | 29.77037773359841 | derived:Ward:raw_markers ; derived:Ward:dimension:fold2 | divide |
| Ward:dimension:fold3 | 1005 | S01: regex ^\\| Ward \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 4 | identity |
| Ward:dimension:fold3:compression | 29.8 | derived:Ward:raw_markers ; derived:Ward:dimension:fold3 | divide |
| Ward:dimension:fold4 | 1010 | S01: regex ^\\| Ward \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 5 | identity |
| Ward:dimension:fold4:compression | 29.65247524752475 | derived:Ward:raw_markers ; derived:Ward:dimension:fold4 | divide |
| Ward:dimension:fold5 | 1005 | S01: regex ^\\| Ward \\| ([\d,]+) \\| (\d+) / (\d+) / (\d+) / (\d+) / (\d+) \\| / group 6 | identity |
| Ward:dimension:fold5:compression | 29.8 | derived:Ward:raw_markers ; derived:Ward:dimension:fold5 | divide |
| Ward:dim_min | 1005 | derived:Ward:dimension:fold1 ; derived:Ward:dimension:fold2 ; derived:Ward:dimension:fold3 ; derived:Ward:dimension:fold4 ; derived:Ward:dimension:fold5 | min |
| Ward:dim_max | 1010 | derived:Ward:dimension:fold1 ; derived:Ward:dimension:fold2 ; derived:Ward:dimension:fold3 ; derived:Ward:dimension:fold4 ; derived:Ward:dimension:fold5 | max |
| Ward:compression_min | 29.65247524752475 | derived:Ward:dimension:fold1:compression ; derived:Ward:dimension:fold2:compression ; derived:Ward:dimension:fold3:compression ; derived:Ward:dimension:fold4:compression ; derived:Ward:dimension:fold5:compression | min |
| Ward:compression_max | 29.8 | derived:Ward:dimension:fold1:compression ; derived:Ward:dimension:fold2:compression ; derived:Ward:dimension:fold3:compression ; derived:Ward:dimension:fold4:compression ; derived:Ward:dimension:fold5:compression | max |
| AUS2015:training_median | 681.9874942302704 | S18: data row 1 / training_seconds_including_epoch_selection ; S18: data row 2 / training_seconds_including_epoch_selection ; S18: data row 3 / training_seconds_including_epoch_selection ; S18: data row 4 / training_seconds_including_epoch_selection ; S18: data row 5 / training_seconds_including_epoch_selection ; S18: data row 6 / training_seconds_including_epoch_selection ; S18: data row 7 / training_seconds_including_epoch_selection ; S18: data row 8 / training_seconds_including_epoch_selection ; S18: data row 9 / training_seconds_including_epoch_selection ; S18: data row 10 / training_seconds_including_epoch_selection ; S18: data row 11 / training_seconds_including_epoch_selection ; S18: data row 12 / training_seconds_including_epoch_selection ; S18: data row 13 / training_seconds_including_epoch_selection ; S18: data row 14 / training_seconds_including_epoch_selection ; S18: data row 15 / training_seconds_including_epoch_selection | median |
| AUS2015:timing_units | 15 | S18: data row 1 / fold ; S18: data row 2 / fold ; S18: data row 3 / fold ; S18: data row 4 / fold ; S18: data row 5 / fold ; S18: data row 6 / fold ; S18: data row 7 / fold ; S18: data row 8 / fold ; S18: data row 9 / fold ; S18: data row 10 / fold ; S18: data row 11 / fold ; S18: data row 12 / fold ; S18: data row 13 / fold ; S18: data row 14 / fold ; S18: data row 15 / fold | count |
| EasyGeSe:lentil:unit1:preparation | 37.42856693267822 | S31: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit1:total | 1411.210901124985 | S31: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit1:share | 0.02652230570415877 | derived:EasyGeSe:lentil:unit1:preparation ; derived:EasyGeSe:lentil:unit1:total | divide |
| EasyGeSe:lentil:unit2:preparation | 43.785667181015015 | S32: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit2:total | 958.6475295000128 | S32: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit2:share | 0.045674417169626086 | derived:EasyGeSe:lentil:unit2:preparation ; derived:EasyGeSe:lentil:unit2:total | divide |
| EasyGeSe:lentil:unit3:preparation | 34.57236099243164 | S33: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit3:total | 554.2226904589916 | S33: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit3:share | 0.06237990899253834 | derived:EasyGeSe:lentil:unit3:preparation ; derived:EasyGeSe:lentil:unit3:total | divide |
| EasyGeSe:lentil:unit4:preparation | 37.70663571357727 | S34: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit4:total | 704.4817900410271 | S34: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit4:share | 0.05352393240907098 | derived:EasyGeSe:lentil:unit4:preparation ; derived:EasyGeSe:lentil:unit4:total | divide |
| EasyGeSe:lentil:unit5:preparation | 37.45915198326111 | S35: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit5:total | 601.4620497500291 | S35: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit5:share | 0.062280158821041716 | derived:EasyGeSe:lentil:unit5:preparation ; derived:EasyGeSe:lentil:unit5:total | divide |
| EasyGeSe:lentil:unit6:preparation | 38.74402475357056 | S36: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit6:total | 796.7805602499866 | S36: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit6:share | 0.04862571539322543 | derived:EasyGeSe:lentil:unit6:preparation ; derived:EasyGeSe:lentil:unit6:total | divide |
| EasyGeSe:lentil:unit7:preparation | 30.247742891311646 | S37: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit7:total | 638.9102092079702 | S37: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit7:share | 0.0473427133506107 | derived:EasyGeSe:lentil:unit7:preparation ; derived:EasyGeSe:lentil:unit7:total | divide |
| EasyGeSe:lentil:unit8:preparation | 39.357293128967285 | S38: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit8:total | 892.222881624999 | S38: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit8:share | 0.044111503907281704 | derived:EasyGeSe:lentil:unit8:preparation ; derived:EasyGeSe:lentil:unit8:total | divide |
| EasyGeSe:lentil:unit9:preparation | 33.31867074966431 | S39: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit9:total | 549.2220625830232 | S39: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit9:share | 0.06066520815453892 | derived:EasyGeSe:lentil:unit9:preparation ; derived:EasyGeSe:lentil:unit9:total | divide |
| EasyGeSe:lentil:unit10:preparation | 40.36021709442139 | S40: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit10:total | 764.183897165989 | S40: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit10:share | 0.05281479660079086 | derived:EasyGeSe:lentil:unit10:preparation ; derived:EasyGeSe:lentil:unit10:total | divide |
| EasyGeSe:lentil:unit11:preparation | 36.8376567363739 | S41: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit11:total | 526.8621721250238 | S41: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit11:share | 0.06991896303314858 | derived:EasyGeSe:lentil:unit11:preparation ; derived:EasyGeSe:lentil:unit11:total | divide |
| EasyGeSe:lentil:unit12:preparation | 43.98388910293579 | S42: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit12:total | 3230.11741024995 | S42: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit12:share | 0.013616808157921502 | derived:EasyGeSe:lentil:unit12:preparation ; derived:EasyGeSe:lentil:unit12:total | divide |
| EasyGeSe:lentil:unit13:preparation | 33.686854124069214 | S43: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit13:total | 566.9075627920101 | S43: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit13:share | 0.059422128641505555 | derived:EasyGeSe:lentil:unit13:preparation ; derived:EasyGeSe:lentil:unit13:total | divide |
| EasyGeSe:lentil:unit14:preparation | 42.1861629486084 | S44: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit14:total | 5205.739930125012 | S44: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit14:share | 0.00810377842820806 | derived:EasyGeSe:lentil:unit14:preparation ; derived:EasyGeSe:lentil:unit14:total | divide |
| EasyGeSe:lentil:unit15:preparation | 33.93778586387634 | S45: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit15:total | 531.5144716249779 | S45: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit15:share | 0.06385110411033534 | derived:EasyGeSe:lentil:unit15:preparation ; derived:EasyGeSe:lentil:unit15:total | divide |
| EasyGeSe:lentil:unit16:preparation | 43.63806104660034 | S46: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit16:total | 4353.782678374962 | S46: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit16:share | 0.010023022339481614 | derived:EasyGeSe:lentil:unit16:preparation ; derived:EasyGeSe:lentil:unit16:total | divide |
| EasyGeSe:lentil:unit17:preparation | 39.376620054244995 | S47: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit17:total | 695.5350516660255 | S47: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit17:share | 0.05661342294673085 | derived:EasyGeSe:lentil:unit17:preparation ; derived:EasyGeSe:lentil:unit17:total | divide |
| EasyGeSe:lentil:unit18:preparation | 27.18840193748474 | S48: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit18:total | 2720.01941899996 | S48: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit18:share | 0.00999566464399758 | derived:EasyGeSe:lentil:unit18:preparation ; derived:EasyGeSe:lentil:unit18:total | divide |
| EasyGeSe:lentil:unit19:preparation | 39.57943391799927 | S49: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit19:total | 741.395449374977 | S49: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit19:share | 0.05338505105658006 | derived:EasyGeSe:lentil:unit19:preparation ; derived:EasyGeSe:lentil:unit19:total | divide |
| EasyGeSe:lentil:unit20:preparation | 26.924216985702515 | S50: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:lentil:unit20:total | 2267.358658000012 | S50: JSON ["total_seconds"] | identity |
| EasyGeSe:lentil:unit20:share | 0.011874705790680591 | derived:EasyGeSe:lentil:unit20:preparation ; derived:EasyGeSe:lentil:unit20:total | divide |
| EasyGeSe:pine:unit21:preparation | 10.308243989944458 | S51: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit21:total | 2308.1629198750015 | S51: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit21:share | 0.004465994969931629 | derived:EasyGeSe:pine:unit21:preparation ; derived:EasyGeSe:pine:unit21:total | divide |
| EasyGeSe:pine:unit22:preparation | 8.752871990203857 | S52: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit22:total | 1266.5952675000299 | S52: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit22:share | 0.006910551629866761 | derived:EasyGeSe:pine:unit22:preparation ; derived:EasyGeSe:pine:unit22:total | divide |
| EasyGeSe:pine:unit23:preparation | 7.996696949005127 | S53: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit23:total | 946.2087793340324 | S53: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit23:share | 0.008451302845269962 | derived:EasyGeSe:pine:unit23:preparation ; derived:EasyGeSe:pine:unit23:total | divide |
| EasyGeSe:pine:unit24:preparation | 11.596353769302368 | S54: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit24:total | 1312.5426832919475 | S54: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit24:share | 0.008835029837062452 | derived:EasyGeSe:pine:unit24:preparation ; derived:EasyGeSe:pine:unit24:total | divide |
| EasyGeSe:pine:unit25:preparation | 8.31361198425293 | S55: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit25:total | 912.8677962499787 | S55: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit25:share | 0.009107136891458858 | derived:EasyGeSe:pine:unit25:preparation ; derived:EasyGeSe:pine:unit25:total | divide |
| EasyGeSe:pine:unit26:preparation | 10.741312980651855 | S56: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit26:total | 763.3995124169742 | S56: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit26:share | 0.01407036919193744 | derived:EasyGeSe:pine:unit26:preparation ; derived:EasyGeSe:pine:unit26:total | divide |
| EasyGeSe:pine:unit27:preparation | 6.703377962112427 | S57: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit27:total | 895.0981274580117 | S57: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit27:share | 0.007488986689257572 | derived:EasyGeSe:pine:unit27:preparation ; derived:EasyGeSe:pine:unit27:total | divide |
| EasyGeSe:pine:unit28:preparation | 11.4984130859375 | S58: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit28:total | 1548.9078609999851 | S58: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit28:share | 0.007423561707869472 | derived:EasyGeSe:pine:unit28:preparation ; derived:EasyGeSe:pine:unit28:total | divide |
| EasyGeSe:pine:unit29:preparation | 6.4778711795806885 | S59: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit29:total | 1254.140973875008 | S59: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit29:share | 0.005165185824019091 | derived:EasyGeSe:pine:unit29:preparation ; derived:EasyGeSe:pine:unit29:total | divide |
| EasyGeSe:pine:unit30:preparation | 11.56750226020813 | S60: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit30:total | 1299.6695849160315 | S60: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit30:share | 0.008900340820821378 | derived:EasyGeSe:pine:unit30:preparation ; derived:EasyGeSe:pine:unit30:total | divide |
| EasyGeSe:pine:unit31:preparation | 6.872908115386963 | S61: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit31:total | 991.2824574169936 | S61: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit31:share | 0.006933349888280935 | derived:EasyGeSe:pine:unit31:preparation ; derived:EasyGeSe:pine:unit31:total | divide |
| EasyGeSe:pine:unit32:preparation | 9.348663091659546 | S62: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit32:total | 1261.9999370420119 | S62: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit32:share | 0.007407815814612303 | derived:EasyGeSe:pine:unit32:preparation ; derived:EasyGeSe:pine:unit32:total | divide |
| EasyGeSe:pine:unit33:preparation | 6.324542999267578 | S63: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit33:total | 1525.4984172499971 | S63: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit33:share | 0.004145886306895537 | derived:EasyGeSe:pine:unit33:preparation ; derived:EasyGeSe:pine:unit33:total | divide |
| EasyGeSe:pine:unit34:preparation | 9.908214092254639 | S64: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit34:total | 1119.355567333987 | S64: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit34:share | 0.008851712879628965 | derived:EasyGeSe:pine:unit34:preparation ; derived:EasyGeSe:pine:unit34:total | divide |
| EasyGeSe:pine:unit35:preparation | 5.927764177322388 | S65: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit35:total | 1006.2219490829739 | S65: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit35:share | 0.005891109990916705 | derived:EasyGeSe:pine:unit35:preparation ; derived:EasyGeSe:pine:unit35:total | divide |
| EasyGeSe:pine:unit36:preparation | 10.010429859161377 | S66: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit36:total | 1090.8873411249951 | S66: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit36:share | 0.009176410323762636 | derived:EasyGeSe:pine:unit36:preparation ; derived:EasyGeSe:pine:unit36:total | divide |
| EasyGeSe:pine:unit37:preparation | 8.27549695968628 | S67: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit37:total | 796.0545107919606 | S67: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit37:share | 0.010395641061631999 | derived:EasyGeSe:pine:unit37:preparation ; derived:EasyGeSe:pine:unit37:total | divide |
| EasyGeSe:pine:unit38:preparation | 10.468071222305298 | S68: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit38:total | 678.9621025830274 | S68: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit38:share | 0.01541775480911352 | derived:EasyGeSe:pine:unit38:preparation ; derived:EasyGeSe:pine:unit38:total | divide |
| EasyGeSe:pine:unit39:preparation | 7.625938892364502 | S69: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit39:total | 1009.6060356250382 | S69: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit39:share | 0.007553380846860083 | derived:EasyGeSe:pine:unit39:preparation ; derived:EasyGeSe:pine:unit39:total | divide |
| EasyGeSe:pine:unit40:preparation | 8.46936297416687 | S70: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:pine:unit40:total | 984.6323873750516 | S70: JSON ["total_seconds"] | identity |
| EasyGeSe:pine:unit40:share | 0.008601548235423669 | derived:EasyGeSe:pine:unit40:preparation ; derived:EasyGeSe:pine:unit40:total | divide |
| EasyGeSe:rice:unit41:preparation | 41.324662923812866 | S71: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit41:total | 1149.0531167910085 | S71: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit41:share | 0.03596410150230597 | derived:EasyGeSe:rice:unit41:preparation ; derived:EasyGeSe:rice:unit41:total | divide |
| EasyGeSe:rice:unit42:preparation | 49.32710123062134 | S72: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit42:total | 851.7227394999936 | S72: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit42:share | 0.05791450544056034 | derived:EasyGeSe:rice:unit42:preparation ; derived:EasyGeSe:rice:unit42:total | divide |
| EasyGeSe:rice:unit43:preparation | 42.359375 | S73: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit43:total | 573.5282691250322 | S73: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit43:share | 0.07385751894082387 | derived:EasyGeSe:rice:unit43:preparation ; derived:EasyGeSe:rice:unit43:total | divide |
| EasyGeSe:rice:unit44:preparation | 45.499549865722656 | S74: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit44:total | 629.9121057910379 | S74: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit44:share | 0.07223158508532668 | derived:EasyGeSe:rice:unit44:preparation ; derived:EasyGeSe:rice:unit44:total | divide |
| EasyGeSe:rice:unit45:preparation | 40.236494064331055 | S75: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit45:total | 628.0004469999694 | S75: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit45:share | 0.06407080481637462 | derived:EasyGeSe:rice:unit45:preparation ; derived:EasyGeSe:rice:unit45:total | divide |
| EasyGeSe:rice:unit46:preparation | 48.181880950927734 | S76: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit46:total | 667.4774801249732 | S76: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit46:share | 0.07218502853745198 | derived:EasyGeSe:rice:unit46:preparation ; derived:EasyGeSe:rice:unit46:total | divide |
| EasyGeSe:rice:unit47:preparation | 45.387288093566895 | S77: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit47:total | 697.9694267919986 | S77: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit47:share | 0.06502761632723024 | derived:EasyGeSe:rice:unit47:preparation ; derived:EasyGeSe:rice:unit47:total | divide |
| EasyGeSe:rice:unit48:preparation | 45.30258512496948 | S78: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit48:total | 707.7469381659757 | S78: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit48:share | 0.06400958122456116 | derived:EasyGeSe:rice:unit48:preparation ; derived:EasyGeSe:rice:unit48:total | divide |
| EasyGeSe:rice:unit49:preparation | 33.53478384017944 | S79: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit49:total | 612.2252059160382 | S79: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit49:share | 0.054775242045128195 | derived:EasyGeSe:rice:unit49:preparation ; derived:EasyGeSe:rice:unit49:total | divide |
| EasyGeSe:rice:unit50:preparation | 44.56260681152344 | S80: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit50:total | 702.0581140840077 | S80: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit50:share | 0.0634742422565194 | derived:EasyGeSe:rice:unit50:preparation ; derived:EasyGeSe:rice:unit50:total | divide |
| EasyGeSe:rice:unit51:preparation | 39.39729118347168 | S81: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit51:total | 598.9017052909476 | S81: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit51:share | 0.06578256638012477 | derived:EasyGeSe:rice:unit51:preparation ; derived:EasyGeSe:rice:unit51:total | divide |
| EasyGeSe:rice:unit52:preparation | 47.74872183799744 | S82: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit52:total | 631.167462708021 | S82: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit52:share | 0.07565143113228899 | derived:EasyGeSe:rice:unit52:preparation ; derived:EasyGeSe:rice:unit52:total | divide |
| EasyGeSe:rice:unit53:preparation | 43.924028158187866 | S83: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit53:total | 672.4574096660363 | S83: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit53:share | 0.06531867673225868 | derived:EasyGeSe:rice:unit53:preparation ; derived:EasyGeSe:rice:unit53:total | divide |
| EasyGeSe:rice:unit54:preparation | 48.02052927017212 | S84: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit54:total | 716.5068738329574 | S84: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit54:share | 0.06702033298478498 | derived:EasyGeSe:rice:unit54:preparation ; derived:EasyGeSe:rice:unit54:total | divide |
| EasyGeSe:rice:unit55:preparation | 43.848042249679565 | S85: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit55:total | 631.8184003750212 | S85: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit55:share | 0.06939975509363638 | derived:EasyGeSe:rice:unit55:preparation ; derived:EasyGeSe:rice:unit55:total | divide |
| EasyGeSe:rice:unit56:preparation | 46.05556011199951 | S86: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit56:total | 651.6659501659451 | S86: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit56:share | 0.07067357148286109 | derived:EasyGeSe:rice:unit56:preparation ; derived:EasyGeSe:rice:unit56:total | divide |
| EasyGeSe:rice:unit57:preparation | 43.47509574890137 | S87: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit57:total | 709.4677739170147 | S87: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit57:share | 0.061278464430981436 | derived:EasyGeSe:rice:unit57:preparation ; derived:EasyGeSe:rice:unit57:total | divide |
| EasyGeSe:rice:unit58:preparation | 46.33708739280701 | S88: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit58:total | 727.3839512080303 | S88: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit58:share | 0.06370375276475504 | derived:EasyGeSe:rice:unit58:preparation ; derived:EasyGeSe:rice:unit58:total | divide |
| EasyGeSe:rice:unit59:preparation | 45.39357590675354 | S89: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit59:total | 700.0275984170148 | S89: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit59:share | 0.06484540896587915 | derived:EasyGeSe:rice:unit59:preparation ; derived:EasyGeSe:rice:unit59:total | divide |
| EasyGeSe:rice:unit60:preparation | 45.797701835632324 | S90: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:rice:unit60:total | 686.945641499944 | S90: JSON ["total_seconds"] | identity |
| EasyGeSe:rice:unit60:share | 0.066668596565564 | derived:EasyGeSe:rice:unit60:preparation ; derived:EasyGeSe:rice:unit60:total | divide |
| EasyGeSe:wheatG:unit61:preparation | 17.046424865722656 | S91: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit61:total | 619.003576374962 | S91: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit61:share | 0.027538491724960194 | derived:EasyGeSe:wheatG:unit61:preparation ; derived:EasyGeSe:wheatG:unit61:total | divide |
| EasyGeSe:wheatG:unit62:preparation | 20.4762601852417 | S92: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit62:total | 611.6938157919794 | S92: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit62:share | 0.033474688899266435 | derived:EasyGeSe:wheatG:unit62:preparation ; derived:EasyGeSe:wheatG:unit62:total | divide |
| EasyGeSe:wheatG:unit63:preparation | 16.125894784927368 | S93: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit63:total | 661.1956738330191 | S93: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit63:share | 0.02438899016299351 | derived:EasyGeSe:wheatG:unit63:preparation ; derived:EasyGeSe:wheatG:unit63:total | divide |
| EasyGeSe:wheatG:unit64:preparation | 17.80089807510376 | S94: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit64:total | 627.2370549580082 | S94: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit64:share | 0.028379857239613306 | derived:EasyGeSe:wheatG:unit64:preparation ; derived:EasyGeSe:wheatG:unit64:total | divide |
| EasyGeSe:wheatG:unit65:preparation | 15.630534172058105 | S95: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit65:total | 468.9818898750236 | S95: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit65:share | 0.033328651936268584 | derived:EasyGeSe:wheatG:unit65:preparation ; derived:EasyGeSe:wheatG:unit65:total | divide |
| EasyGeSe:wheatG:unit66:preparation | 19.204046964645386 | S96: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit66:total | 511.03791091701714 | S96: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit66:share | 0.03757851727709446 | derived:EasyGeSe:wheatG:unit66:preparation ; derived:EasyGeSe:wheatG:unit66:total | divide |
| EasyGeSe:wheatG:unit67:preparation | 14.487957000732422 | S97: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit67:total | 405.85452595801326 | S97: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit67:share | 0.03569741391089289 | derived:EasyGeSe:wheatG:unit67:preparation ; derived:EasyGeSe:wheatG:unit67:total | divide |
| EasyGeSe:wheatG:unit68:preparation | 17.947146892547607 | S98: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit68:total | 478.66568712500157 | S98: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit68:share | 0.03749411619692887 | derived:EasyGeSe:wheatG:unit68:preparation ; derived:EasyGeSe:wheatG:unit68:total | divide |
| EasyGeSe:wheatG:unit69:preparation | 15.918750047683716 | S99: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit69:total | 552.0762840419775 | S99: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit69:share | 0.028834330522470555 | derived:EasyGeSe:wheatG:unit69:preparation ; derived:EasyGeSe:wheatG:unit69:total | divide |
| EasyGeSe:wheatG:unit70:preparation | 18.860853910446167 | S100: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit70:total | 588.2864118329599 | S100: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit70:share | 0.032060665572200206 | derived:EasyGeSe:wheatG:unit70:preparation ; derived:EasyGeSe:wheatG:unit70:total | divide |
| EasyGeSe:wheatG:unit71:preparation | 13.79401969909668 | S101: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit71:total | 357.78567000001203 | S101: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit71:share | 0.03855386298477582 | derived:EasyGeSe:wheatG:unit71:preparation ; derived:EasyGeSe:wheatG:unit71:total | divide |
| EasyGeSe:wheatG:unit72:preparation | 18.247778177261353 | S102: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit72:total | 491.12744124996243 | S102: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit72:share | 0.03715487395861888 | derived:EasyGeSe:wheatG:unit72:preparation ; derived:EasyGeSe:wheatG:unit72:total | divide |
| EasyGeSe:wheatG:unit73:preparation | 14.896911144256592 | S103: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit73:total | 381.1860019589658 | S103: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit73:share | 0.039080425481784156 | derived:EasyGeSe:wheatG:unit73:preparation ; derived:EasyGeSe:wheatG:unit73:total | divide |
| EasyGeSe:wheatG:unit74:preparation | 18.373000860214233 | S104: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit74:total | 436.5248124169884 | S104: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit74:share | 0.04208924747824759 | derived:EasyGeSe:wheatG:unit74:preparation ; derived:EasyGeSe:wheatG:unit74:total | divide |
| EasyGeSe:wheatG:unit75:preparation | 16.176271200180054 | S105: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit75:total | 444.9252940000151 | S105: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit75:share | 0.03635727484663864 | derived:EasyGeSe:wheatG:unit75:preparation ; derived:EasyGeSe:wheatG:unit75:total | divide |
| EasyGeSe:wheatG:unit76:preparation | 18.875932216644287 | S106: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit76:total | 2331.751918833994 | S106: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit76:share | 0.008095171730826025 | derived:EasyGeSe:wheatG:unit76:preparation ; derived:EasyGeSe:wheatG:unit76:total | divide |
| EasyGeSe:wheatG:unit77:preparation | 16.811051845550537 | S107: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit77:total | 436.9363490000251 | S107: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit77:share | 0.038474830221894796 | derived:EasyGeSe:wheatG:unit77:preparation ; derived:EasyGeSe:wheatG:unit77:total | divide |
| EasyGeSe:wheatG:unit78:preparation | 18.472821950912476 | S108: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit78:total | 1516.3075627500075 | S108: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit78:share | 0.012182767140862751 | derived:EasyGeSe:wheatG:unit78:preparation ; derived:EasyGeSe:wheatG:unit78:total | divide |
| EasyGeSe:wheatG:unit79:preparation | 15.714190244674683 | S109: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit79:total | 512.9410730000236 | S109: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit79:share | 0.03063546881275768 | derived:EasyGeSe:wheatG:unit79:preparation ; derived:EasyGeSe:wheatG:unit79:total | divide |
| EasyGeSe:wheatG:unit80:preparation | 19.170166969299316 | S110: JSON ["full_fit_preprocessing_seconds"] | identity |
| EasyGeSe:wheatG:unit80:total | 3885.324829042016 | S110: JSON ["total_seconds"] | identity |
| EasyGeSe:wheatG:unit80:share | 0.004933993375793499 | derived:EasyGeSe:wheatG:unit80:preparation ; derived:EasyGeSe:wheatG:unit80:total | divide |
| EasyGeSe:preparation_median | 23.700238585472107 | derived:EasyGeSe:lentil:unit1:preparation ; derived:EasyGeSe:lentil:unit2:preparation ; derived:EasyGeSe:lentil:unit3:preparation ; derived:EasyGeSe:lentil:unit4:preparation ; derived:EasyGeSe:lentil:unit5:preparation ; derived:EasyGeSe:lentil:unit6:preparation ; derived:EasyGeSe:lentil:unit7:preparation ; derived:EasyGeSe:lentil:unit8:preparation ; derived:EasyGeSe:lentil:unit9:preparation ; derived:EasyGeSe:lentil:unit10:preparation ; derived:EasyGeSe:lentil:unit11:preparation ; derived:EasyGeSe:lentil:unit12:preparation ; derived:EasyGeSe:lentil:unit13:preparation ; derived:EasyGeSe:lentil:unit14:preparation ; derived:EasyGeSe:lentil:unit15:preparation ; derived:EasyGeSe:lentil:unit16:preparation ; derived:EasyGeSe:lentil:unit17:preparation ; derived:EasyGeSe:lentil:unit18:preparation ; derived:EasyGeSe:lentil:unit19:preparation ; derived:EasyGeSe:lentil:unit20:preparation ; derived:EasyGeSe:pine:unit21:preparation ; derived:EasyGeSe:pine:unit22:preparation ; derived:EasyGeSe:pine:unit23:preparation ; derived:EasyGeSe:pine:unit24:preparation ; derived:EasyGeSe:pine:unit25:preparation ; derived:EasyGeSe:pine:unit26:preparation ; derived:EasyGeSe:pine:unit27:preparation ; derived:EasyGeSe:pine:unit28:preparation ; derived:EasyGeSe:pine:unit29:preparation ; derived:EasyGeSe:pine:unit30:preparation ; derived:EasyGeSe:pine:unit31:preparation ; derived:EasyGeSe:pine:unit32:preparation ; derived:EasyGeSe:pine:unit33:preparation ; derived:EasyGeSe:pine:unit34:preparation ; derived:EasyGeSe:pine:unit35:preparation ; derived:EasyGeSe:pine:unit36:preparation ; derived:EasyGeSe:pine:unit37:preparation ; derived:EasyGeSe:pine:unit38:preparation ; derived:EasyGeSe:pine:unit39:preparation ; derived:EasyGeSe:pine:unit40:preparation ; derived:EasyGeSe:rice:unit41:preparation ; derived:EasyGeSe:rice:unit42:preparation ; derived:EasyGeSe:rice:unit43:preparation ; derived:EasyGeSe:rice:unit44:preparation ; derived:EasyGeSe:rice:unit45:preparation ; derived:EasyGeSe:rice:unit46:preparation ; derived:EasyGeSe:rice:unit47:preparation ; derived:EasyGeSe:rice:unit48:preparation ; derived:EasyGeSe:rice:unit49:preparation ; derived:EasyGeSe:rice:unit50:preparation ; derived:EasyGeSe:rice:unit51:preparation ; derived:EasyGeSe:rice:unit52:preparation ; derived:EasyGeSe:rice:unit53:preparation ; derived:EasyGeSe:rice:unit54:preparation ; derived:EasyGeSe:rice:unit55:preparation ; derived:EasyGeSe:rice:unit56:preparation ; derived:EasyGeSe:rice:unit57:preparation ; derived:EasyGeSe:rice:unit58:preparation ; derived:EasyGeSe:rice:unit59:preparation ; derived:EasyGeSe:rice:unit60:preparation ; derived:EasyGeSe:wheatG:unit61:preparation ; derived:EasyGeSe:wheatG:unit62:preparation ; derived:EasyGeSe:wheatG:unit63:preparation ; derived:EasyGeSe:wheatG:unit64:preparation ; derived:EasyGeSe:wheatG:unit65:preparation ; derived:EasyGeSe:wheatG:unit66:preparation ; derived:EasyGeSe:wheatG:unit67:preparation ; derived:EasyGeSe:wheatG:unit68:preparation ; derived:EasyGeSe:wheatG:unit69:preparation ; derived:EasyGeSe:wheatG:unit70:preparation ; derived:EasyGeSe:wheatG:unit71:preparation ; derived:EasyGeSe:wheatG:unit72:preparation ; derived:EasyGeSe:wheatG:unit73:preparation ; derived:EasyGeSe:wheatG:unit74:preparation ; derived:EasyGeSe:wheatG:unit75:preparation ; derived:EasyGeSe:wheatG:unit76:preparation ; derived:EasyGeSe:wheatG:unit77:preparation ; derived:EasyGeSe:wheatG:unit78:preparation ; derived:EasyGeSe:wheatG:unit79:preparation ; derived:EasyGeSe:wheatG:unit80:preparation | median |
| EasyGeSe:total_median | 703.2699520625174 | derived:EasyGeSe:lentil:unit1:total ; derived:EasyGeSe:lentil:unit2:total ; derived:EasyGeSe:lentil:unit3:total ; derived:EasyGeSe:lentil:unit4:total ; derived:EasyGeSe:lentil:unit5:total ; derived:EasyGeSe:lentil:unit6:total ; derived:EasyGeSe:lentil:unit7:total ; derived:EasyGeSe:lentil:unit8:total ; derived:EasyGeSe:lentil:unit9:total ; derived:EasyGeSe:lentil:unit10:total ; derived:EasyGeSe:lentil:unit11:total ; derived:EasyGeSe:lentil:unit12:total ; derived:EasyGeSe:lentil:unit13:total ; derived:EasyGeSe:lentil:unit14:total ; derived:EasyGeSe:lentil:unit15:total ; derived:EasyGeSe:lentil:unit16:total ; derived:EasyGeSe:lentil:unit17:total ; derived:EasyGeSe:lentil:unit18:total ; derived:EasyGeSe:lentil:unit19:total ; derived:EasyGeSe:lentil:unit20:total ; derived:EasyGeSe:pine:unit21:total ; derived:EasyGeSe:pine:unit22:total ; derived:EasyGeSe:pine:unit23:total ; derived:EasyGeSe:pine:unit24:total ; derived:EasyGeSe:pine:unit25:total ; derived:EasyGeSe:pine:unit26:total ; derived:EasyGeSe:pine:unit27:total ; derived:EasyGeSe:pine:unit28:total ; derived:EasyGeSe:pine:unit29:total ; derived:EasyGeSe:pine:unit30:total ; derived:EasyGeSe:pine:unit31:total ; derived:EasyGeSe:pine:unit32:total ; derived:EasyGeSe:pine:unit33:total ; derived:EasyGeSe:pine:unit34:total ; derived:EasyGeSe:pine:unit35:total ; derived:EasyGeSe:pine:unit36:total ; derived:EasyGeSe:pine:unit37:total ; derived:EasyGeSe:pine:unit38:total ; derived:EasyGeSe:pine:unit39:total ; derived:EasyGeSe:pine:unit40:total ; derived:EasyGeSe:rice:unit41:total ; derived:EasyGeSe:rice:unit42:total ; derived:EasyGeSe:rice:unit43:total ; derived:EasyGeSe:rice:unit44:total ; derived:EasyGeSe:rice:unit45:total ; derived:EasyGeSe:rice:unit46:total ; derived:EasyGeSe:rice:unit47:total ; derived:EasyGeSe:rice:unit48:total ; derived:EasyGeSe:rice:unit49:total ; derived:EasyGeSe:rice:unit50:total ; derived:EasyGeSe:rice:unit51:total ; derived:EasyGeSe:rice:unit52:total ; derived:EasyGeSe:rice:unit53:total ; derived:EasyGeSe:rice:unit54:total ; derived:EasyGeSe:rice:unit55:total ; derived:EasyGeSe:rice:unit56:total ; derived:EasyGeSe:rice:unit57:total ; derived:EasyGeSe:rice:unit58:total ; derived:EasyGeSe:rice:unit59:total ; derived:EasyGeSe:rice:unit60:total ; derived:EasyGeSe:wheatG:unit61:total ; derived:EasyGeSe:wheatG:unit62:total ; derived:EasyGeSe:wheatG:unit63:total ; derived:EasyGeSe:wheatG:unit64:total ; derived:EasyGeSe:wheatG:unit65:total ; derived:EasyGeSe:wheatG:unit66:total ; derived:EasyGeSe:wheatG:unit67:total ; derived:EasyGeSe:wheatG:unit68:total ; derived:EasyGeSe:wheatG:unit69:total ; derived:EasyGeSe:wheatG:unit70:total ; derived:EasyGeSe:wheatG:unit71:total ; derived:EasyGeSe:wheatG:unit72:total ; derived:EasyGeSe:wheatG:unit73:total ; derived:EasyGeSe:wheatG:unit74:total ; derived:EasyGeSe:wheatG:unit75:total ; derived:EasyGeSe:wheatG:unit76:total ; derived:EasyGeSe:wheatG:unit77:total ; derived:EasyGeSe:wheatG:unit78:total ; derived:EasyGeSe:wheatG:unit79:total ; derived:EasyGeSe:wheatG:unit80:total | median |
| EasyGeSe:preparation_share_median | 0.03675607440262876 | derived:EasyGeSe:lentil:unit1:share ; derived:EasyGeSe:lentil:unit2:share ; derived:EasyGeSe:lentil:unit3:share ; derived:EasyGeSe:lentil:unit4:share ; derived:EasyGeSe:lentil:unit5:share ; derived:EasyGeSe:lentil:unit6:share ; derived:EasyGeSe:lentil:unit7:share ; derived:EasyGeSe:lentil:unit8:share ; derived:EasyGeSe:lentil:unit9:share ; derived:EasyGeSe:lentil:unit10:share ; derived:EasyGeSe:lentil:unit11:share ; derived:EasyGeSe:lentil:unit12:share ; derived:EasyGeSe:lentil:unit13:share ; derived:EasyGeSe:lentil:unit14:share ; derived:EasyGeSe:lentil:unit15:share ; derived:EasyGeSe:lentil:unit16:share ; derived:EasyGeSe:lentil:unit17:share ; derived:EasyGeSe:lentil:unit18:share ; derived:EasyGeSe:lentil:unit19:share ; derived:EasyGeSe:lentil:unit20:share ; derived:EasyGeSe:pine:unit21:share ; derived:EasyGeSe:pine:unit22:share ; derived:EasyGeSe:pine:unit23:share ; derived:EasyGeSe:pine:unit24:share ; derived:EasyGeSe:pine:unit25:share ; derived:EasyGeSe:pine:unit26:share ; derived:EasyGeSe:pine:unit27:share ; derived:EasyGeSe:pine:unit28:share ; derived:EasyGeSe:pine:unit29:share ; derived:EasyGeSe:pine:unit30:share ; derived:EasyGeSe:pine:unit31:share ; derived:EasyGeSe:pine:unit32:share ; derived:EasyGeSe:pine:unit33:share ; derived:EasyGeSe:pine:unit34:share ; derived:EasyGeSe:pine:unit35:share ; derived:EasyGeSe:pine:unit36:share ; derived:EasyGeSe:pine:unit37:share ; derived:EasyGeSe:pine:unit38:share ; derived:EasyGeSe:pine:unit39:share ; derived:EasyGeSe:pine:unit40:share ; derived:EasyGeSe:rice:unit41:share ; derived:EasyGeSe:rice:unit42:share ; derived:EasyGeSe:rice:unit43:share ; derived:EasyGeSe:rice:unit44:share ; derived:EasyGeSe:rice:unit45:share ; derived:EasyGeSe:rice:unit46:share ; derived:EasyGeSe:rice:unit47:share ; derived:EasyGeSe:rice:unit48:share ; derived:EasyGeSe:rice:unit49:share ; derived:EasyGeSe:rice:unit50:share ; derived:EasyGeSe:rice:unit51:share ; derived:EasyGeSe:rice:unit52:share ; derived:EasyGeSe:rice:unit53:share ; derived:EasyGeSe:rice:unit54:share ; derived:EasyGeSe:rice:unit55:share ; derived:EasyGeSe:rice:unit56:share ; derived:EasyGeSe:rice:unit57:share ; derived:EasyGeSe:rice:unit58:share ; derived:EasyGeSe:rice:unit59:share ; derived:EasyGeSe:rice:unit60:share ; derived:EasyGeSe:wheatG:unit61:share ; derived:EasyGeSe:wheatG:unit62:share ; derived:EasyGeSe:wheatG:unit63:share ; derived:EasyGeSe:wheatG:unit64:share ; derived:EasyGeSe:wheatG:unit65:share ; derived:EasyGeSe:wheatG:unit66:share ; derived:EasyGeSe:wheatG:unit67:share ; derived:EasyGeSe:wheatG:unit68:share ; derived:EasyGeSe:wheatG:unit69:share ; derived:EasyGeSe:wheatG:unit70:share ; derived:EasyGeSe:wheatG:unit71:share ; derived:EasyGeSe:wheatG:unit72:share ; derived:EasyGeSe:wheatG:unit73:share ; derived:EasyGeSe:wheatG:unit74:share ; derived:EasyGeSe:wheatG:unit75:share ; derived:EasyGeSe:wheatG:unit76:share ; derived:EasyGeSe:wheatG:unit77:share ; derived:EasyGeSe:wheatG:unit78:share ; derived:EasyGeSe:wheatG:unit79:share ; derived:EasyGeSe:wheatG:unit80:share | median |
| EasyGeSe:preparation_share_percent | 3.6756074402628762 | derived:EasyGeSe:preparation_share_median | percent |
| LR:PCC_range_min | 0.0040890312194824 | S14: data row 2 / range_across_tier_means ; S14: data row 3 / range_across_tier_means ; S14: data row 4 / range_across_tier_means ; S14: data row 5 / range_across_tier_means | min |
| LR:PCC_range_max | 0.0146393334865569 | S14: data row 2 / range_across_tier_means ; S14: data row 3 / range_across_tier_means ; S14: data row 4 / range_across_tier_means ; S14: data row 5 / range_across_tier_means | max |
| LR:lentil:PCC_range | 0.0068269157409668 | S14: data row 2 / range_across_tier_means | identity |
| LR:pine:PCC_range | 0.0110074865818023 | S14: data row 3 / range_across_tier_means | identity |
| LR:rice:PCC_range | 0.0040890312194824 | S14: data row 4 / range_across_tier_means | identity |
| LR:wheatG:PCC_range | 0.0146393334865569 | S14: data row 5 / range_across_tier_means | identity |

## 9. 复现与账本

每张图表的脚本独立保存在 `scripts/`。`scripts/run_all.py` 只读取源文件并做表格汇总/作图，不执行训练或实验。默认推断原项目根目录，也支持 `AGRIFORMER_SOURCE_ROOT` 与 `AGRIFORMER_ARTIFACT_OUT`。复现包集成文件暂存于本目录 `experiments/`，遵守“所有新输出写入 data/”的约束；未写入外部 release 仓库。

原账本已存在同名 FIG-DATA-20261028 的历史完成行。本轮保留旧行，按任务要求追加同 ID 的复核修订行；新行明确修复、真实检查和未记录项，供按最后一次记录读取的下游使用。


## v2 修订（10/28）

### 修订范围与旧版保全

修订前的 v1 构建已完整复制到 previous_build/v1_20261028/，并生成 SHA256SUMS.txt；本轮没有删除、移动或改写任何实验结果。当前构建只读取冻结结果，重新汇总表格、作图和生成溯源记录。

### F1--F10 实际改动

- **F1（Table III）**：由实验批次改为每个模型一行；同一模型跨配置逐数据集、逐指标取最优记录，BayesB 仅纳入修正截距的 HF1_E6 结果；SVR-RBF 保留。AF 使用种子均值预测的指标，另报告逐种子均值 ± 样本标准差。
- **F2（Table I）**：删除 AF 列中的“(1/1 method)”，修正破折号引号，并把表注改为面向论文读者的范围、分母和符号说明。
- **F3（Table IV）**：Perm 行按三个小麦固定留出集的臂中位数计算。MT−Perm 的三群体均值为 **+0.020871**；retained 按 AUS2015/GABI/Ward 顺序为 **0.8963/0.9449/0.4367**，表中显示为 +0.021; retained 0.90/0.94/0.44。该差值不是逐对差。
- **F4（Table V）**：准备耗时口径限定为 lentil、pine、rice 和 wheatG；从 80 个正式 EasyGeSe AF-MT/AF-ST 单元的 JSON 逐单元计算 preparation/total，其中位数为 **3.675607%**（显示 3.68%），准备时间中位数 23.7002 s，总耗时中位数 703.2700 s。
- **F5（Fig. 3）**：压缩上方空白并把图例移入不遮挡数据的位置；图注明确 7/7 数据集尺度项大于排序项绝对值，Ward 的 Δln PCC = −0.104。
- **F6（Fig. 4）**：样本比例小图固定为 Ridge、MLP-Dual；标记比例小图固定为 BayesB、Ridge，并加入与样本比例小图共享的 100% 配置。缺失小图用实心 AF/空心 GBLUP 区分，(d) 的数据集标签重新避让且保留描述性 ρ = −0.679。
- **F7（Fig. 5）**：(a) 改为 naive − scoped 高估量；7 个数据集 × 2 个学习器 × 2 个指标的 **28/28** 个值均为正（范围 0.0777--0.6138）。(b) 保留小麦难度秩翻转并修复 AUS2015 标签贴边。
- **F8（图注/表注）**：全部改为论文读者用语，去除任务执行说明，明确协议、统计量定义、数据范围和缺失值含义。
- **F9（Table III 可比模型子集）**：只保留在 AUS2015、GABI 和 Ward 三个固定留出集上都有结果的 13 个模型，加 AF 共 14 个条目；逐数据集、逐指标在这 14 个条目中重算排名和前三名格式。另有 30 个只在 AUS2015 上评估的回归器未列入；完整结果位于 `pilot_20261013/holdout_fill_20261027/HOLDOUT_FULL_PANEL.csv`。
- **F10（Table III 表注）**：对 30 个 AUS2015-only 回归器的结果位置改用面向论文读者的说明：结果提供于发布的 artifact。

### Table III 配置→模型完整映射

Included=False 的四个旧 BayesB 配置因未采用修正截距而排除；其余配置按算法身份归并。机器可读版本为 table_iii_config_model_map.csv。

| Configuration | Model | Included | Rule |
|---|---|---:|---|
| `E6H::BayesB_long_s42` | BayesB | False | corrected intercept only |
| `E6H::BayesB_long_s43` | BayesB | False | corrected intercept only |
| `E6H::BayesB_short_s42` | BayesB | False | corrected intercept only |
| `E6H::BayesB_short_s43` | BayesB | False | corrected intercept only |
| `E6H::GBLUP_rrBLUP_mean` | GBLUP | True | collapsed by algorithm identity |
| `E6H::RF_default` | RF | True | collapsed by algorithm identity |
| `E6H::Ridge_default` | Ridge | True | collapsed by algorithm identity |
| `E6H::SVR-RBF_default` | SVR-RBF | True | collapsed by algorithm identity |
| `HF1_E6::BayesB_long_s42` | BayesB | True | corrected intercept only |
| `HF1_E6::BayesB_long_s43` | BayesB | True | corrected intercept only |
| `HF1_E6::BayesB_short_s42` | BayesB | True | corrected intercept only |
| `HF1_E6::BayesB_short_s43` | BayesB | True | corrected intercept only |
| `HF1_N_tuned::GBLUP` | GBLUP | True | collapsed by algorithm identity |
| `HF1_N_tuned::MLP-Dual` | MLP-Dual | True | collapsed by algorithm identity |
| `HF1_N_tuned::RF` | RF | True | collapsed by algorithm identity |
| `HF1_N_tuned::Ridge` | Ridge | True | collapsed by algorithm identity |
| `HF1_N_tuned::SVR-RBF` | SVR-RBF | True | collapsed by algorithm identity |
| `HF1_N_tuned::VMGP` | VMGP | True | collapsed by algorithm identity |
| `HF2_deep::Cropformer` | Cropformer | True | collapsed by algorithm identity |
| `HF2_deep::DeepGS` | DeepGS | True | collapsed by algorithm identity |
| `HF2_deep::WheatGP` | WheatGP | True | collapsed by algorithm identity |
| `HF2_v8_tuned::ElasticNet` | ElasticNet | True | collapsed by algorithm identity |
| `HF2_v8_tuned::LightGBM` | LightGBM | True | collapsed by algorithm identity |
| `TabNet::raw_seed_mean` | TabNet | True | collapsed by algorithm identity |
| `VMGP::seed_mean` | VMGP | True | collapsed by algorithm identity |
| `deep_adapted::Cropformer` | Cropformer | True | collapsed by algorithm identity |
| `deep_adapted::DPCformer` | DPCformer | True | collapsed by algorithm identity |
| `deep_adapted::DeepGS` | DeepGS | True | collapsed by algorithm identity |
| `deep_adapted::GEFormer` | GEFormer | True | collapsed by algorithm identity |
| `deep_adapted::GP_WAITER` | GP-WAITER | True | collapsed by algorithm identity |
| `deep_adapted::GPformer` | GPformer | True | collapsed by algorithm identity |
| `deep_adapted::LSTM` | LSTM | True | collapsed by algorithm identity |
| `deep_adapted::WheatGP` | WheatGP | True | collapsed by algorithm identity |
| `v8_tuned::AdaBoost` | AdaBoost | True | collapsed by algorithm identity |
| `v8_tuned::BayesianRidge` | BayesianRidge | True | collapsed by algorithm identity |
| `v8_tuned::CART` | CART | True | collapsed by algorithm identity |
| `v8_tuned::DecisionTree_pruned` | Decision tree | True | collapsed by algorithm identity |
| `v8_tuned::ElasticNet` | ElasticNet | True | collapsed by algorithm identity |
| `v8_tuned::ExtraTrees` | ExtraTrees | True | collapsed by algorithm identity |
| `v8_tuned::GaussianProcess_RBF` | GaussianProcess_RBF | True | collapsed by algorithm identity |
| `v8_tuned::GaussianRP_Ridge` | GaussianRP_Ridge | True | collapsed by algorithm identity |
| `v8_tuned::GradientBoosting` | GradientBoosting | True | collapsed by algorithm identity |
| `v8_tuned::HistGradientBoosting` | HistGradientBoosting | True | collapsed by algorithm identity |
| `v8_tuned::HuberRegressor` | HuberRegressor | True | collapsed by algorithm identity |
| `v8_tuned::KNN_distance` | KNN_distance | True | collapsed by algorithm identity |
| `v8_tuned::KernelRidge_RBF` | KernelRidge_RBF | True | collapsed by algorithm identity |
| `v8_tuned::Lasso` | Lasso | True | collapsed by algorithm identity |
| `v8_tuned::LightGBM` | LightGBM | True | collapsed by algorithm identity |
| `v8_tuned::LightGBM_extra_regularized` | LightGBM | True | collapsed by algorithm identity |
| `v8_tuned::LinearSVR` | LinearSVR | True | collapsed by algorithm identity |
| `v8_tuned::NuSVR_RBF` | NuSVR_RBF | True | collapsed by algorithm identity |
| `v8_tuned::NystroemRBF_Ridge` | NystroemRBF_Ridge | True | collapsed by algorithm identity |
| `v8_tuned::OrthogonalMatchingPursuit` | OrthogonalMatchingPursuit | True | collapsed by algorithm identity |
| `v8_tuned::PCR_Ridge` | PCR_Ridge | True | collapsed by algorithm identity |
| `v8_tuned::PLSRegression` | PLSRegression | True | collapsed by algorithm identity |
| `v8_tuned::PassiveAggressive` | PassiveAggressive | True | collapsed by algorithm identity |
| `v8_tuned::RBFSampler_Ridge` | RBFSampler_Ridge | True | collapsed by algorithm identity |
| `v8_tuned::RF` | RF | True | collapsed by algorithm identity |
| `v8_tuned::RandomTanhFeatures_Ridge` | RandomTanhFeatures_Ridge | True | collapsed by algorithm identity |
| `v8_tuned::Ridge` | Ridge | True | collapsed by algorithm identity |
| `v8_tuned::SVR` | SVR-RBF | True | collapsed by algorithm identity |
| `v8_tuned::SVR_RBF` | SVR-RBF | True | collapsed by algorithm identity |
| `v8_tuned::SparseRP_Ridge` | SparseRP_Ridge | True | collapsed by algorithm identity |
| `v8_tuned::TruncatedSVD_Ridge` | TruncatedSVD_Ridge | True | collapsed by algorithm identity |
| `v8_tuned::TweedieRegressor` | TweedieRegressor | True | collapsed by algorithm identity |

### AF 排名与逐种子统计

| Dataset | AF rank PCC/CCC | Per-seed PCC mean ± SD | Per-seed CCC mean ± SD | Seeds |
|---|---:|---:|---:|---:|
| AUS2015 | 6/8 | 0.810 ± 0.006 | 0.758 ± 0.052 | 20 |
| GABI | 4/2 | 0.609 ± 0.012 | 0.578 ± 0.018 | 5 |
| Ward | 9/1 | 0.388 ± 0.024 | 0.373 ± 0.026 | 5 |

排名仅在表内 14 个条目中计算；并列采用 1e−12 容差下的最小名次。因此 6/8、4/2 和 9/1 分别表示 PCC 名次/CCC 名次，不是名次/分母。表内 AF 主数值是种子均值预测的评分，而不是逐种子指标的算术均值，因此两行数值不要求相等。

### 逐格溯源与自检

- 8 个图表共有 **1,135** 个数值/派生元素通过源文件重算：Table I 18、Table II 77、Table III 261、Table IV 176、Table V 297、Fig. 3 42、Fig. 4 194、Fig. 5 70。Table III 元素数减少来自按可比性规则移除 AUS2015-only 行；Table V 元素数减少来自确认的四数据集、80 单元耗时口径。两项均未修改任何实验结果。
- 每个元素的来源、原始行/列、运算和输出值分别保存在对应 *_evidence.json 与 *_provenance.csv；绘图数据和表格数据保存在 *_source_data.csv。
- Fig. 4 在筛选、排序和拼接共享 100% 行后仍保留原 CSV 行号；本轮逐格验证确认没有把排序后的行号误作源行号。
- 三张图均为单页矢量 PDF，宽度分别为 3.50、7.16、7.16 in，8 pt 字体，字体嵌入，并生成 300 dpi PNG；所有文字均在画布内。
- 五张表用 IEEEtran conference 双栏模板联合编译为 5 页，**0 个溢出警告、0 个未定义引用**；最终页面已逐页渲染检查。
- 35 个冻结源文件通过哈希复核；账本按任务要求另行追加。验证汇总见 qa/VALIDATION.json。

### 仍需记录的问题

1. ICDE_story_v7_framework_v1_1_20261028.md 在本轮开始前已相对 v1 的源清单发生外部变化；本轮未修改该文件，也未把它作为数值来源。其旧版仍保存在 v1 构建副本中，故该预存漂移未被误报为本轮修改。
