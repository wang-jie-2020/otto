---
name: frontend-slides
description: 从零创建或通过转换 PowerPoint 文件，生成惊艳、动画丰富的 HTML 演示文稿。适用于用户希望制作演示、将 PPT/PPTX 转为网页，或为演讲/提案创建幻灯片的场景。通过可视化探索而非抽象选项，帮助非设计师找到自己的审美方向。
---

# Frontend Slides

创建零依赖、动画丰富、完全在浏览器中运行的 HTML 演示文稿。

## 核心原则

1. **零依赖** — 单个 HTML 文件，内联 CSS/JS。不用 npm，不用构建工具。
2. **少讲多看** — 生成可视化预览，而不是抽象选项。人们通过“看到”来判断自己想要什么。
3. **有辨识度的设计** — 避免通用的“AI 味”设计。每份演示都必须像定制打磨过的作品。
4. **渐进披露** — 先读轻量风格索引。对于大胆模板，先用小预览卡展示风格，用户选中后再加载完整 `design.md`。
5. **固定 16:9 舞台（不可妥协）** — 每个 deck 都使用 1920×1080 画布，并整体缩放适配视口。所有屏幕（含手机）都必须保持 16:9。不要为了设备去重排幻灯片内容。

## 设计审美

你倾向于收敛到通用、均值化的输出。在前端设计中，这会形成用户常说的“AI 味”审美。要避免这一点：做出有创意、有辨识度、能带来惊喜的前端。

重点关注：

- Typography（字体）：选择漂亮、独特、有趣的字体。避免 Arial、Inter 等常见字体；优先选择能提升整体气质的字体。
- Color & Theme（配色与主题）：坚持统一审美。使用 CSS 变量确保一致性。主色鲜明 + 点缀利落，通常优于平均分配的保守配色。可从 IDE 主题和文化审美中获取灵感。
- Motion（动效）：用动画塑造效果与微交互。HTML 优先 CSS-only；React 可用 Motion 库。聚焦高影响力时刻：一次编排良好的入场（如 staggered reveal + `animation-delay`）比零散微动效更有愉悦感。
- Backgrounds（背景）：营造氛围和层次，不要默认纯色底。叠加 CSS 渐变、几何图案或与整体审美一致的情境化效果。

避免常见 AI 生成审美：

- 过度使用的字体族（Inter、Roboto、Arial、系统字体）
- 陈词滥调式配色（尤其白底紫色渐变）
- 可预测的布局与组件模式
- 缺少场景特征的模板化设计

要有创造性地解读并做出意料之外但合理的选择，让设计真正贴合语境。在明暗主题、字体、审美方向上保持变化。你仍然容易在多次生成中收敛到常见选择（例如 Space Grotesk）。必须避免，务必跳出惯性。

## 固定舞台规则

以下不变量适用于每一份演示中的每一页幻灯片：

- 每个 deck 都有一个充满浏览器窗口的 viewport wrapper。
- 每页幻灯片都在固定的 1920×1080 舞台内编排。
- 舞台等比缩放以适配视口。可以有黑边（letterbox/pillarbox），但禁止重排内容。
- 不要为手机使用响应式断点重排幻灯片内容。
- 幻灯片内部尺寸按 1920×1080 设计尺寸固定。
- 幻灯片显隐必须通过 `.active` / `.visible` 配合 `viewport-base.css` 中的 `visibility`、`opacity`、`pointer-events` 控制。切换幻灯片时不要使用 `display: none` / `display: block`；后续布局类（如 `.slide-content { display: flex; }`）可能覆盖它们并导致所有幻灯片同时可见。
- `clamp()` 仅可用于舞台外的非幻灯片 UI，或完整舞台不适用的小型兜底预览。
- 包含 `prefers-reduced-motion` 支持。
- 永远不要直接对 CSS 函数取负（`-clamp()`、`-min()`、`-max()` 会被静默忽略）— 应使用 `calc(-1 * clamp(...))`。

**生成时，必须读取 `viewport-base.css`，并在每个演示中完整包含其全部内容。**

### 内容密度模式

询问用户该 deck 主要用于“阅读”还是“演讲”，并据此设计：

| 密度模式 | 适用场景 | 设计行为 |
| ------------- | -------- | --------------- |
| **低密度 / 演讲驱动** | 公开演讲、Keynote 风格分享、现场讲解 | 每页一个观点、大字号、强层级、充足留白、最多 1-3 条 bullet，必要时增加页数 |
| **高密度 / 阅读优先** | 报告、讲义、异步评审、详细内部文档 | 更多自包含页面、结构化网格/表格/注释，可读前提下 4-8 条 bullet 或 4-6 张卡片，间距更紧凑但有意图 |

基础限制始终有效：不滚动、不溢出、不重叠，文字不得小于舒适阅读尺寸。若内容超出所选密度模式，应拆分为更多页面，而不是一味缩小导致拥挤。

---

## 阶段 0：识别模式

判断用户想要什么：

- **模式 A：新建演示** — 从零创建。进入阶段 1。
- **模式 B：PPT 转换** — 转换 `.pptx` 文件。进入阶段 4。
- **模式 C：增强改造** — 改进现有 HTML 演示。先阅读并理解，再增强。**遵循下方模式 C 修改规则。**

### 模式 C：修改规则

增强现有演示时，固定舞台适配是最大风险：

1. **加内容前：** 统计现有元素，核对密度上限。
2. **加图片：** 图片必须放进 1920×1080 画布。若页面内容已满，拆成两页。
3. **加文字：** 每页最多 4-6 条 bullet。超限就拆分续页。
4. **任何修改后都要验证：** 舞台仍为 16:9；文字不溢出卡片；面板不重叠；在 1280×720 与至少一个手机视口截图都正常。
5. **主动重组：** 若修改会导致溢出，自动拆分并告知用户，不要等用户提醒。

**向现有页面加图片时：** 先把图片移到新页，或先减少其他内容。绝不能在未检查内容是否已占满 1920×1080 舞台前直接加图。

---

## 阶段 1：内容发现（新建演示）

**在一次 AskUserQuestion 调用中提完所有问题**，让用户一次填完：

**问题 1 — 目的**（header: "Purpose"）：
这个演示用于什么？选项：Pitch deck / Teaching-Tutorial / Conference talk / Internal presentation

**问题 2 — 长度**（header: "Length"）：
大约多少页？选项：Short 5-10 / Medium 10-20 / Long 20+

**问题 3 — 内容**（header: "Content"）：
你是否已有内容？选项：All content ready / Rough notes / Topic only

**问题 4 — 密度**（header: "Density"）：
希望 deck 的信息密度如何？选项：

- "Low density / speaker-led" — 大观点、少文字、更多视觉呼吸空间
- "High density / reading-first" — 更自包含的细节，适合异步阅读

**阶段 1 不要询问内联编辑。** 用户在看到草稿前不该被迫选择编辑方式。内联编辑属于草稿后的能力：默认启用，除非用户明确要求仅锁定/仅导出文件。

记住用户的密度选择。它影响页数、字号、文字量、布局紧凑度，以及偏向“演讲型”还是“阅读型”页面。

如果用户已有内容，要求其提供。

### 步骤 1.2：图片评估（若提供图片）

若用户选择 “No images” → 直接跳到阶段 2。

若用户提供图片文件夹：

1. **扫描** — 列出全部图片文件（`.png`、`.jpg`、`.svg`、`.webp` 等）
2. **逐张查看** — 使用 Read 工具（Claude 具备多模态）
3. **评估** — 对每张给出：画面内容、USABLE 或 NOT USABLE（含原因）、代表概念、主导色
4. **协同设计大纲** — 精选图片应与文本共同决定结构。这不是“先规划页面再塞图”，而是从一开始围绕两者共同设计（例如 3 张截图 → 3 页功能页，1 个 logo → 标题/结尾页）
5. **通过 AskUserQuestion 确认**（header: "Outline"）："这个页面大纲和图片选择是否合适？" 选项：Looks good / Adjust images / Adjust outline

**预览中的 Logo：** 若识别出可用 logo，在阶段 2 的每个风格预览中内嵌它（base64），让用户看到同一品牌在三种风格下的表现。

---

## 阶段 2：风格发现

**这是“少讲多看”阶段。** 多数人无法准确用语言描述设计偏好。

### 步骤 2.0：直接生成 3 个风格预览

基于目的、受众、氛围和内容密度，生成 3 个单页 HTML 预览，展示字体、配色、动画和整体美学。

不要询问用户是否需要选项或预设选择器。默认发现流程始终是可视化对比。

若用户已给 vibe，则使用；否则根据场景、受众、内容和 stakes 推断情绪方向。选项要足够多样，便于用户通过“看”来反馈，而非先抽象表达审美。

若用户明确指定某个 preset 或大胆模板，将其作为一个选项，并围绕它生成其余预览。

读取 [STYLE_PRESETS.md](STYLE_PRESETS.md) 获取安全预设候选。若存在 [bold-template-pack/selection-index.json](bold-template-pack/selection-index.json)，也读取该紧凑索引，但此时不要读取任何 `design.md`。

| 情绪                | 推荐预设                                  |
| ------------------- | -------------------------------------------------- |
| Impressed/Confident | Bold Signal, Electric Studio, Dark Botanical       |
| Excited/Energized   | Creative Voltage, Neon Cyber, Split Pastel         |
| Calm/Focused        | Notebook Tabs, Paper & Ink, Swiss Modern           |
| Inspired/Moved      | Dark Botanical, Vintage Editorial, Pastel Geometry |

**预览组合规则：**

- 默认生成 3 个预览：1 个来自 `STYLE_PRESETS.md` 的安全预设，至少 1 个来自 `bold-template-pack/selection-index.json` 的大胆模板，另加 1 个 wildcard。
- wildcard 可为第二个大胆模板，也可为自生成自定义设计。选择最能针对用户场景、受众、情绪和内容形成有效对比的方案。
- 不要强制把所有表现型选项都来自模板库。如果任务存在比模板更尖锐、更具体的设计机会，用 wildcard 自由设计。
- 对保守或高风险演示：安全预设应更克制；大胆模板选择更平稳且正式；wildcard 也应偏权威而非装饰。
- 对表现型演示：保留一个可读性安全选项；选择一个强表达的大胆模板；wildcard 应更冒险、更贴场景，并与其他两项明显不同。
- 若大胆模板匹配不理想，可将 wildcard 设为自定义设计，或回退为另一个安全预设，不要硬套模板。

**自定义 wildcard 规则：**

- 遵循上文“设计审美”：拒绝通用“AI 味”，拒绝默认字体/配色/布局，拒绝白底紫渐变陈词滥调，拒绝千篇一律仪表盘/卡片风。
- 匹配用户给定的场景、受众、情绪/vibe 和内容密度。自定义设计要像为此 deck 专门创作，而非泛化“好看”。
- 建立明确视觉论点：独特字体、坚定调色、可识别布局系统，以及一个强氛围/图形装置。
- 保证可扩展成整套 deck。预览应隐含可延展到章节页、内容页、引语页、对比页、结尾页的设计系统。
- 遵守固定 1920×1080 舞台规则，并通过与其他方案相同的真实性检查。
- 幻灯片本身不要出现“custom”“wildcard”“AI-generated”或设计流程标签。

**大胆模板选择规则：**

- 按 `mood`、`tone`、`best_for`、`avoid_for`、`formality`、`density`、`scheme` 匹配用户需求。
- 将 `best_for` 示例视为弱信号，而非严格行业过滤。
- 三个预览必须彼此真正不同。
- 确定候选后，仅读取候选模板在 selection index 中 `preview_md` 指向的 `preview.md`。
- `preview.md` 仅用于标题页预览。用户未最终选择前，不要读完整 `design.md`。
- 除非选中的最终 `design.md` 缺少关键实现细节，否则不要读取或拷贝 `template.html`。

**预览真实性规则（不可妥协）：**

- 每个风格预览必须像用户真实 deck 的首页，而不是诊断卡片。
- 不要在幻灯片中渲染内部流程文本：如 `preview`、`generated from`、`preview.md`、`template`、`preset`、`style option`、`Option A/B/C`、文件名、路径或来源文档标签。
- 不要在幻灯片本身显示模板名或 slug。模板/风格名称只应出现在与用户的消息里。
- 不要把用户需求备注直接当作页面文案，如 “sharp and provocative”“safe option”“bold option”“for internal sharing”“audience: ...”，除非用户明确要求这些原句入稿。
- 若需要页面 chrome，只能用真实 deck chrome：标题、章节标题、日期、作者、公司、页码，或用户材料中的真实短语。
- 打开预览前，检查可见文本；如有内部元数据，先修正。

将预览保存到 `.claude-design/slide-previews/`（`style-a.html`、`style-b.html`、`style-c.html`）。每个预览都应自包含且紧凑，展示一张带动画的标题页。

自动为用户打开每个预览。

### 步骤 2.1：用户选择

提问（header: "Style"）：
你更喜欢哪个风格预览？选项：Style A: [Name] / Style B: [Name] / Style C: [Name] / Mix elements

若选择 “Mix elements”，继续追问具体要混合哪些元素。

---

## 阶段 3：生成演示

基于阶段 1 的内容（纯文本或文本 + 精选图片）和阶段 2 的风格生成完整演示。

如果提供了图片，步骤 1.2 已把它们并入页面大纲。若无图片，可使用 CSS 生成视觉元素（渐变、形状、图案）补足视觉吸引力，这是完全受支持的一等路径。

在整套 deck 中贯彻用户的密度选择：

- **低密度 / 演讲驱动：** 更多页面、每页更少信息。强调大标题、短语、视觉隐喻、章节节奏、引语/观点页，以及友好的演讲节拍。
- **高密度 / 阅读优先：** 页面更自包含。使用结构化网格、对比表、注释图、说明性 caption 与精炼解释文案。层级要强，保证“像设计过的页面”，而非“把文档贴到幻灯片”。

若用户需求混合，二选一靠近原则，不要硬造中间态：现场说服型默认低密度；异步流转或细节审阅默认高密度。

绝不允许高密度变成视觉杂乱。若页面开始溢出，拆页或重构布局。

若用户从 `bold-template-pack` 选了大胆模板，生成前只读取该模板的完整 `design.md`，不要读取其他模板。将 `design.md` 视为设计配方：

- 保留其字体、调色、装饰语汇、间距节奏和组件语法。
- 无论原模板使用 `deck-stage.js` 还是 viewport-fluid CSS，最终都必须生成为固定 1920×1080 舞台并等比缩放到视口。
- 将 `design.md` 中 viewport-fluid 数值当作比例参考，转译为 1920×1080 舞台坐标；不要在最终成品中保留实时视口重排规则。
- 输出必须是单文件、完全自包含的 Frontend Slides HTML。
- 不要拷贝示例页内容，也不要过度照搬源模板。
- `template.html` 仅在所选模板实现细节缺失时作为兜底参考。
- 生成后同时验证文本溢出与面板重叠（基于浏览器截图）。仅看 `scrollHeight` 不够，因为网格面板可能视觉互相覆盖。

若用户选择了自生成 wildcard，自该预览的 CSS 与布局中提炼设计配方：

- 保留其字体、调色、装饰语汇、间距节奏、网格逻辑和组件语法。
- 用同一视觉系统扩展整套 deck。用户选定自定义方向后，不要切换回 preset 或大胆模板。
- 缺失的页面类型应基于该系统补齐，而非引入其他风格模式。
- 与其他 deck 一样，保持固定舞台、单文件输出，并完成视觉验证。

**生成前必须读取以下支持文件：**

- [html-template.md](html-template.md) — HTML 架构与 JS 功能
- [viewport-base.css](viewport-base.css) — 强制 CSS（完整包含）
- [animation-patterns.md](animation-patterns.md) — 与目标情绪匹配的动画参考

**关键要求：**

- 单个自包含 HTML 文件，所有 CSS/JS 内联
- 在 `<style>` 块中包含 `viewport-base.css` 全量内容
- 字体来自 Fontshare 或 Google Fonts，禁止系统字体
- 添加详细注释说明每个区块
- 每个区块都要有清晰的 `/* === SECTION NAME === */` 注释块

---

## 阶段 4：PPT 转换

转换 PowerPoint 文件时：

1. **提取内容** — 运行 `python scripts/extract-pptx.py <input.pptx> <output_dir>`（若缺依赖，先安装 `python-pptx`：`pip install python-pptx`）
2. **与用户确认** — 展示提取出的页面标题、内容摘要和图片数量
3. **风格选择** — 进入阶段 2 做风格发现
4. **生成 HTML** — 转换为所选风格，保留所有文本、图片（来自 assets/）、页面顺序和讲者备注（以 HTML 注释保存）

---

## 阶段 5：交付

1. **清理** — 若存在 `.claude-design/slide-previews/` 则删除
2. **打开** — 使用 `open [filename].html` 在浏览器中启动
3. **总结** — 告诉用户：
   - 文件位置、风格名称、页数
   - 导航方式：方向键、空格，若启用则支持滑动/点按
   - 如何定制：` :root` CSS 变量改色、字体链接改字体、`.reveal` 类控制动画
   - 支持内联编辑：悬停左上角或按 E 进入编辑模式，点击任意文本可编辑，Ctrl+S 保存
   - 提供自然的后续动作：继续改稿、直接在浏览器改文案、或导出/分享

---

## 阶段 6：分享与导出（可选）

交付后，**询问用户：** _“你想分享这个演示吗？我可以部署为在线链接（任何设备含手机都可访问），或者导出为 PDF。”_

选项：

- **部署到 URL** — 可分享链接，任意设备可访问
- **导出 PDF** — 通用文件，便于邮件、Slack、打印
- **两者都要**
- **不用了**

若用户拒绝，到此结束。若选择其一或两者，继续执行。

### 6A：部署到在线 URL（Vercel）

将演示部署到 Vercel（免费托管平台）。链接可在手机、平板、笔记本访问，并会一直在线，直到用户手动下线。

**若用户从未部署过，按步骤引导：**

1. **检查是否安装 Vercel CLI** — 运行 `npx vercel --version`。若未安装，先安装 Node.js（macOS 可 `brew install node`，或从 https://nodejs.org 下载）。

2. **检查登录状态** — 运行 `npx vercel whoami`。
   - 若未登录，说明：_“Vercel 是免费托管服务。你需要一个账号才能部署。我带你一步步来：”_
     - 第 1 步：让用户在浏览器打开 https://vercel.com/signup
     - 第 2 步：可用 GitHub、Google 或邮箱注册
     - 第 3 步：注册后运行 `vercel login` 并按提示授权（会打开浏览器）
     - 第 4 步：用 `vercel whoami` 确认登录
   - 继续前需等待用户确认已登录。

3. **执行部署** — 运行部署脚本：

   ```bash
   bash scripts/deploy.sh <path-to-presentation>
   ```

   脚本接受文件夹（含 `index.html`）或单个 HTML 文件。

4. **分享链接** — 告诉用户：
   - 在线 URL（来自脚本输出）
   - 该链接可在任意设备访问，可发短信、Slack、邮件
   - 后续下线方式：访问 https://vercel.com/dashboard 删除项目
   - Vercel 免费额度充足，不会自动收费

**部署注意事项：**

- **本地图片/视频必须随 HTML 一起部署。** 脚本会自动检测 HTML 中 `src="..."` 引用并打包，但 CSS `background-image` 或非常规路径可能漏掉。**部署后务必检查**：打开线上 URL 确认图片都能加载。若有缺图，最稳妥方案是把 HTML 与资源放进同一文件夹并部署文件夹，而不是只部署单文件。
- **资源多时优先部署文件夹。** 若演示结构是 `my-deck/index.html` + 同目录资源（如 `my-deck/logo.png`），请直接 `bash scripts/deploy.sh ./my-deck/`。这通常比单 HTML 更可靠，因为会原样上传整个目录。
- **文件名带空格虽可用但可能出问题。** 脚本能处理空格，但 URL 会编码为 `%20`。若可能，尽量避免图片文件名含空格。若仍缺图，重命名为连字符是常见修复方式。
- **重复部署会更新同一 URL。** 再次运行部署脚本会覆盖此前部署，URL 保持不变，无需重新分享。

### 6B：导出为 PDF

该流程会对每页截图并合并成 PDF，适合邮件附件、文档嵌入或打印。

**说明：** 动画与交互不会保留，PDF 是静态快照。这是正常现象，应提前告知用户。

1. **运行导出脚本：**

   ```bash
   bash scripts/export-pdf.sh <path-to-html> [output.pdf]
   ```

   若未提供输出路径，PDF 默认与 HTML 放在同目录。

2. **幕后过程**（向用户简述）：
   - 无头浏览器以 1920×1080（标准宽屏）打开演示
   - 按页逐张截图
   - 将所有截图合并为一个 PDF
   - 需要 Playwright（浏览器自动化工具），缺失时会自动安装

3. **若 Playwright 安装失败：**
   - 最常见是 Chromium 下载失败。运行：`npx playwright install chromium`
   - 若仍失败，可能是网络/防火墙问题，建议用户换网络重试

4. **交付 PDF** — 脚本会自动打开 PDF。告知用户：
   - 文件位置与大小
   - 通用可用场景：邮件、Slack、Notion、Google Docs、打印
   - 动画会被替换为最终视觉状态（依然美观，只是静态）

**PDF 导出注意事项：**

- **首次运行较慢。** 脚本会安装 Playwright 并下载 Chromium（约 150MB）到临时目录。通常首次约 30-60 秒；同会话后续导出更快。
- **幻灯片必须使用 `class="slide"`。** 导出脚本通过查询 `.slide` 获取页面。若类名不同，会报 “0 slides found” 并失败。本技能生成的演示默认都使用 `.slide`，此问题主要出现在外部 HTML。
- **本地图片必须可通过 HTTP 访问。** 脚本会启动本地服务再加载 HTML（确保 Google Fonts 和相对路径可用）。若图片使用绝对文件系统路径（如 `src="/Users/name/photo.png"`）而非相对路径（如 `src="photo.png"`），将无法加载。生成演示默认是相对路径，转换或外部提供文件需检查修正。
- **相对路径图片可正常出现在 PDF 中。** 脚本会以 HTML 的父目录作为 HTTP 根目录，`src="photo.png"` 这类相对路径可正确解析（含空格文件名）。若仍不显示，检查：1）引用路径对应的文件确实存在；2）路径是相对路径，而不是 `/Users/name/photo.png` 这类绝对文件系统路径。
- **页数多会导致 PDF 体积大。** 每页按 1920×1080 PNG 截图。18 页可能约 20MB。若超过 10MB，询问用户：_“当前 PDF 为 [size]。要我压缩吗？清晰度会略降，但体积会显著变小。”_ 若同意，使用 `--compact` 重新导出：
  ```bash
  bash scripts/export-pdf.sh <path-to-html> [output.pdf] --compact
  ```
  此模式以 1280×720 渲染，通常可减少 50-70% 体积，视觉差异很小。

---

## 支持文件

| 文件                                               | 作用                                                              | 何时读取              |
| -------------------------------------------------- | -------------------------------------------------------------------- | ------------------------- |
| [STYLE_PRESETS.md](STYLE_PRESETS.md)               | 12 套精选视觉预设（配色、字体、标志性元素） | 阶段 2（风格选择） |
| [bold-template-pack/selection-index.json](bold-template-pack/selection-index.json) | 大胆模板候选选择用的紧凑元数据 | 阶段 2（风格选择） |
| [bold-template-pack/templates/*/preview.md](bold-template-pack/templates/) | 入围大胆模板的轻量风格卡（标题页预览） | 阶段 2 入围后 |
| [bold-template-pack/templates/*/design.md](bold-template-pack/templates/) | 仅对最终选中大胆模板读取的详细设计系统文档 | 阶段 3 用户选定后 |
| [viewport-base.css](viewport-base.css)             | 强制固定舞台 CSS — 每个演示都要拷贝进去             | 阶段 3（生成）      |
| [html-template.md](html-template.md)               | HTML 结构、JS 功能、代码质量标准                  | 阶段 3（生成）      |
| [animation-patterns.md](animation-patterns.md)     | CSS/JS 动画片段与“效果-情绪”映射指南                | 阶段 3（生成）      |
| [scripts/extract-pptx.py](scripts/extract-pptx.py) | PPT 内容提取 Python 脚本                             | 阶段 4（转换）      |
| [scripts/deploy.sh](scripts/deploy.sh)             | 将演示部署到 Vercel 以便即时分享                          | 阶段 6（分享）         |
| [scripts/export-pdf.sh](scripts/export-pdf.sh)     | 将演示导出为 PDF                                                 | 阶段 6（分享）         |

