---
name: demo-prototype-generator
description: Design and generate product demo prototypes from product documents, PRDs, business flows, feature lists, screenshots, reference designs, or product descriptions. Use when Codex needs to create HTML demos, static demo images, HTML plus images, mobile H5 or app demos, PC web or admin demos, multi-end linked demos, report-ready demos for customers, government, leadership, internal reviews, solution presentations, interface explanation demos, or data dashboard demos.
---

# Demo Prototype Generator

Design product demos for customer reports, government reports, internal reviews, solution presentations, and business or technical demonstrations. The output may be a runnable HTML prototype, static image, HTML plus image, mobile H5/app demo, PC web/admin demo, multi-end linked demo, or a demo that includes interface information.

Core rule: if required information is missing, stop and ask once. Do not silently invent unspecified product scope, style, interface fields, or page behavior.

## Required Inputs

Before generating a demo, confirm these required items:

| Input | Required | Notes |
|---|---:|---|
| Product document or description | Yes | Background, target users, core functions, business process, and page scope. |
| End type | Yes | User end, merchant end, receiving end, enterprise end, operations backend, H5, app, PC web, etc. |
| Design style | Yes | Reference PPT, screenshots, colors, style keywords, brand rules, or visual direction. |
| Output format | Yes | HTML, image, HTML plus image, etc. |
| Interface information needed | Yes | Need / do not need. |
| Interface information | Conditional | Required if the demo must show interfaces, integrations, fields, or interface granularity. |
| Page scope | Yes | Pages, functions, or flows to cover. |

Optional but useful: audience, demo emphasis, interaction requirements, language, size ratio, and forbidden content.

### Missing Information Rule

If any required item is missing, do not start generation. Ask in one message:

```text
我现在还不能开始生成 Demo，因为缺少以下必要信息：
1. 产品文档 / 产品说明：请提供产品背景、核心功能或业务流程。
2. 端类型：这是用户端、商户端、收货端、企业端、运营后台，还是其他端？
3. 设计风格：是否有参考 PPT、截图、色值或风格要求？
4. 输出格式：需要 HTML、图片，还是 HTML+图片？
5. 是否需要接口信息：需要 / 不需要？
6. 页面范围：需要覆盖哪些页面或功能？
请补充以上信息后，我再开始设计，避免自行脑补。
```

If the user says interface information is needed but does not provide it, ask for interface name, integration party, purpose, input fields, output fields, and trigger page or business node.

## Workflow

### 1. Parse the user input

Extract:

- Product name, background, target users, and end type.
- Core business scenarios, functions, page scope, and process.
- Status transitions, data sources, external systems, interface relationships, and key fields.
- Reporting emphasis and explicit forbidden content.

Ask first if key information is absent.

### 2. Select the demo type

Choose the demo type from the request:

- Product prototype demo: show how users operate the product.
- Business process demo: show an end-to-end business chain.
- Multi-end collaboration demo: show user, merchant, backend, delivery, airport, bank, logistics, or other ends working together.
- Interface explanation demo: show APIs, fields, integrations, and triggered actions behind functions.
- Report-oriented demo: emphasize value and user experience for customers, government, or leaders.
- Data dashboard demo: show metrics, filters, drill-downs, and analysis results.
- Mobile H5/app demo: show mobile process and interactions.
- PC web/admin demo: show management, review, query, configuration, reconciliation, and operational functions.

### 3. Design the page structure

Before generation, organize pages in a compact table:

| Page | Goal | Core content | Main actions | Navigation | Interface information |
|---|---|---|---|---|---|

Use real business language from the user input. Avoid invalid placeholders such as "Interface 1" or "Field A" unless the user explicitly allows placeholders.

### 4. Confirm interaction scope

For HTML demos, define the interactions before building. Common interactions:

- Page switching, tab switching, popups, drill-downs, filters, search, forms, status switching, scrolling.
- Multilingual switching, simulated scanning, simulated upload, toast feedback.
- Left-right linked views, interface console linkage, and multi-end status synchronization.

If the user did not specify interactions, confirm the scope before adding complex interactions.

### 5. Output the demo blueprint before generating

Before producing HTML or images, output a demo blueprint and wait for confirmation unless the user explicitly says to generate directly and all required inputs are complete.

The blueprint must include:

- Demo type judgment.
- Page structure table.
- Page navigation relationships.
- Interaction list.
- Interface display method.
- Visual style direction.
- Output format.

Suggested confirmation wording:

```text
这是我为您设计的 Demo 蓝图，包含 X 个页面、Y 个核心交互、Z 个接口展示点。请确认是否符合预期。收到您的“行”或修改意见后，我再正式生成完整 HTML / 图片。
```

### 6. Generate the demo

Generate according to the confirmed format:

- HTML: produce a directly runnable single-file demo.
- Image: produce static visuals in the requested ratio and style.
- HTML plus image: provide both interactive and presentation assets.

## Interface Information Rules

Only use interface names, fields, integration parties, and response data provided by the user. If interface data is insufficient, ask first.

Organize interface information by page, function, or process node:

| Page / node | Function | Interface | Integration party | Trigger | Input fields | Output fields | Notes |
|---|---|---|---|---|---|---|---|

For multi-end demos, use:

| End type | Page | Function | Interface | Integration party | Fields | Notes |
|---|---|---|---|---|---|---|

### Interface presentation methods

Do not place large interface tables directly inside the product UI. Prefer:

- Developer control panel.
- Right-side interface console.
- Floating interface panel.
- Info icon hover/click detail.
- Split-screen view with product on the left and live interface logs on the right.
- Drawer panel opened from an action.

Recommended behavior: when the user clicks a product action such as "提交退税申请", the product UI changes state and the right-side console logs the relevant interface call with request, response, and status.

## Multi-End Demo Rules

When multiple ends are shown, define each end's boundary before building:

- Role, core goal, main functions, page scope, relationship with other ends, data source, and interface relationship.

Common end types:

- User end: application, query, payment, status tracking.
- Merchant end: order entry, product or invoice sync, pickup preparation.
- Receiving end: query, verification, delivery confirmation.
- Enterprise end: management, query, reconciliation, configuration.
- Operations/admin backend: review, monitoring, exceptions, configuration, statistics.
- Airport, bank, logistics, or other specialized ends.

Do not mix capabilities across ends unless explicitly requested. A multi-end demo must show state synchronization, not just static screens placed side by side.

## HTML Output Standards

### Basic

- Output one HTML file that can open directly.
- Keep HTML, CSS, and JS in the same file unless the user requests otherwise.
- Do not require a backend service.
- Implement required page switches, popups, drill-downs, scrolling, filters, and state changes.
- Use a mobile container for mobile demos, a horizontal layout for PC web demos, and 16:9 for report demos.
- Avoid flicker, layout shift, overlap, clipped text, horizontal overflow, and content spilling outside containers.
- Make the UI feel like a modern real product, not an early static web page or table mockup.

### CSS and Tailwind

If the user allows external CSS/CDN, Tailwind CDN may be used for development speed and modern styling. Do not use unstable CDNs, duplicate frameworks, broken icon libraries, or unreachable image resources.

If the user requires offline operation, do not use CDN or Tailwind class names. Use in-file standard CSS with modern layout, spacing, border radius, shadows, and hierarchy. Keep CSS focused on the demo.

### No dead links

Every button, menu, card, and link must have clear feedback. Avoid `href="#"` and inert buttons.

Use `javascript:void(0);` or bind a toast such as:

```text
功能演示：[功能名]已触发
```

### Data-driven mock content

Use JavaScript arrays or state objects to simulate real data sources for lists, tables, orders, records, logistics status, users, merchants, notifications, metrics, interface logs, filters, search results, and pagination.

Search, filtering, pagination, and detail popups should render from these arrays so the demo feels operable rather than static.

### Multi-end state synchronization

For multi-end demos, use shared global state. When one end changes state, re-render the other ends and interface console. Example: user submits an application, backend pending list updates, status changes, and interface log appears.

### Interaction robustness

Verify:

- All clickable elements respond.
- Tabs switch.
- Modals open and close.
- Drill-down works.
- Search and filters change results.
- Empty states are handled.
- Loading states end.
- Long lists scroll.
- Interface panels do not block the main flow.
- Mobile content does not overflow horizontally.
- PC tables, buttons, and filters fit cleanly.

## Image Output Standards

Before generating image demos, confirm:

- Ratio, size, number of pages, whether each page is a separate image, whether only partial assets are needed, transparent background requirements, whether to preserve source PPT style, and whether layout or color may be changed.

If the user asks only for a partial asset, do not generate a full page. If the user says not to change unrelated content, modify only the specified area.

## Visual Style Rules

If the user provides a reference image, PPT, or HTML, follow its main color, background, card style, radius, icon style, typography, density, spacing, shadow, and report structure.

If the user provides only a broad style keyword, map it as follows and confirm in the blueprint:

| Style keyword | Visual atoms |
|---|---|
| Technology / dashboard | Dark #0B1120, neon blue/cyan #38BDF8, subtle grid, data cards, map or flow lines. |
| Government / enterprise backend | White or light gray #F8FAFC, deep blue #1E40AF or restrained red accents, standard tables, clear filters, strict hierarchy. |
| Mobile H5 / consumer app | Large radius, light shadow, ample whitespace, clear CTA, card information, bottom navigation. |
| Finance / payment | Deep blue, gold or green accents, prominent amount numbers, account cards, clear status and risk prompts. |
| Logistics / supply chain | Blue-gray palette, maps, routes, timeline nodes, status labels, exception alerts, progress bars. |
| Government report page | 16:9, stable background, restrained highlights, visual plus data, policy/value/process loop emphasis. |
| Customer solution demo | More polished visuals, before/after contrast, efficiency gains, product highlights, split or scenario storytelling. |

If the style remains unclear, ask for reference image/PPT, preferred main color, light or dark direction, and whether it should be a real product prototype or report page.

## Content Organization

Prioritize:

- The current role's core task.
- Key business status.
- Necessary action buttons.
- Key data and process nodes.
- Necessary interface or field information.

Avoid:

- Long explanatory prose.
- Feature piling.
- Overdense information.
- Excess decoration.
- In-product labels such as "设计说明", "下钻入口说明", or "这里展示".
- Meaningless placeholders unless explicitly allowed.

## Final Checks

Before delivery, check:

- Business: matches the product description, does not omit required features, does not mix end types, does not change business flow, and does not invent interfaces or fields.
- Visual: matches requested style, color, background, layout, and product realism; no overlap, tiny text, clutter, or unrelated decoration.
- Interaction: opens correctly; buttons, tabs, modals, drill-downs, scroll, search, filters, pagination, language switch, multi-end sync, and interface console work where required; no dead links, empty jumps, flicker, or jitter.

## User Input Template

```text
【产品文档 / 产品说明】请粘贴产品说明，或上传 PRD / PPT / 截图 / 业务流程说明。
【端类型】例如：用户端 H5 / 商户端 APP / 收货端 APP / 企业端 PC 后台 / 多端联动。
【设计风格】例如：参考附件 PPT；蓝色科技风；政务简洁风；沿用某张截图风格；主色 #XXXXXX。
【输出格式】HTML / 图片 / HTML+图片。
【是否需要接口信息】需要 / 不需要。
【接口信息】如需要，请提供接口名称、对接方、用途、字段、触发页面或业务节点。
【页面范围】需要展示哪些页面、功能或流程。
【交互要求】是否需要点击、切换、下钻、弹窗、筛选、滚动、多语言、接口控制台联动、多端状态同步。
【语言要求】中文 / 英文 / 中英双语 / 多语种切换。
【尺寸比例】手机竖屏 / Web 横屏 / 16:9 / 其他。
【禁止事项】不要出现哪些内容、不要改哪些内容、不要新增哪些功能。
```
