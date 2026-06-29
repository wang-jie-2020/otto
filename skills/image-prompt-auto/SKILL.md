---
name: image-prompt-auto
description: 图像生成**提示词创建指南**
disable-model-invocation: true
---

# Image Prompt

**提示词创建指南**

## 技能结构
  - `references`
    - `references/prompt-writing.md`：结构化提示词书写指导
    - `references/index.md`：模板索引

## 工作步骤

1. 识别用户任务所属分类，先在 `references/index.md` 中定位最相关模板。
2. 只读取对应模板文件，不要一次性读取整个 `references/`。
3. 严格遵循模板格式：大部分模板用 JSON 主模板（结构化任务首选），少数模板（`infographics/hand-drawn-infographic.md`、`academic-figures/scientific-schematic.md` 等）使用「结构化自然语言 + 参数」混合形式，因为强行 JSON 会限制创作自由。
4. 把用户输入映射到模板参数；关键信息不足时主动发起有针对性的澄清问题。
5. 输出完整最终 prompt，并保存到 `./prompts/`。

默认命名规则：
  - `<task-slug>-<timestamp>.md`
  - `<task-slug>`：根据用户要求提取短名称
  - `<timestamp>`：例如 `20260424-153045`
示例：
  - `live-commerce-ui-20260424-153045.md`
  - `vr-headset-exploded-view-20260424-153102.md`

## JSON 模板工作方式

当 `references/` 中提供 JSON 模板时，按下面规则使用：

1. 先从 `index.md` 找到最贴近的分类目录。
2. 再定位到具体模板文件。
3. 模板中的 `{argument ...}` 表示可替换参数。
4. 用户明确提供的值，直接填入。
5. 用户没有提供，但模板标了 `default` 的，默认可以先用默认值。
6. 如果缺失信息会显著影响结果，主动询问用户。
7. 用户也可以明确说“你随机生成”，这时可以保留默认值或在模板允许范围内合理随机化。

## 何时提问
只在这些信息缺失且会显著影响结果时提问：

- 没有 prompt 目标
- 改图时没有原图
- 主体身份或视觉类型决定结果走向
- 商品 / 价格 / 文案 / UI 文本是画面核心组成部分
- 用户同时表达了多个互相冲突的目标

除此之外，优先自己做合理默认并继续执行。

当模板缺少关键变量时，不要笼统地问“你想要什么风格？”。应当根据模板字段精确提问。
例如直播 UI 模板缺少主体时，应优先问：

- 主播是谁？
- 用真人照片、名人名字、人物描述，还是完全随机生成？

缺少商品信息时应问：

- 商品名称是什么？
- 商品价格是否指定？
- 是否希望我自动补全评论和礼物内容？


