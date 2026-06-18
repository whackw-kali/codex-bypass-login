# Codex 登录不上?这个能救你

**登录 Codex CLI 失败时的兜底方案** — 用 ChatGPT session token 直接配 `~/.codex/auth.json`,跳过 OAuth / 验证码 / 短信验证。

## 怎么用

1. 浏览器登录 [chatgpt.com](https://chatgpt.com)
2. 新开标签,访问 `chatgpt.com/api/auth/session`,`Ctrl+A` 复制返回的 JSON
3. 打开 [index.html](./index.html),把 JSON 粘到第二步的输入框
4. 选你系统(Windows / Linux / macOS),命令自动生成
5. 复制命令,粘到终端回车

或者点"AI 一键跑"按钮,生成一段给 AI agent 的指令,让 AI 帮你跑 + 验证。

## 安全

- **100% 本地运行** — 所有 token 处理在浏览器里,不会上传到任何服务器
- **可断网验证** — 另存 index.html 断网打开,所有功能照样用
- **代码完全可见** — 没有混淆/加密/外发

## 局限(必看)

- **token 约 10 天过期**(OAuth 标准),过期需要重新跑一次
- **本工具不提供自动续期**(因为拿不到 refresh_token)
- 想真正"一劳永逸"自动续期,用 Codex 官方 `codex login`(浏览器 OAuth)

## 原理

等价于 Codex CLI 官方的 `codex login --with-access-token` 命令。本工具做的是纯前端版本,数据全在本地。

## 免责声明

- 这个工具只读你自己浏览器里 ChatGPT session 的 token,不绕过任何 ChatGPT 安全机制
- 你的 token 自己保管,不要发给任何人,不要截图发群里
- 用 ChatGPT Plus 订阅登录 Codex 需自行确认是否符合 OpenAI 服务条款
- 作者不为使用此工具导致的任何账号问题负责

## 链接

- [Codex CLI 官方认证文档](https://developers.openai.com/codex/auth)
- [openai/codex 源码](https://github.com/openai/codex)
- [Codex CLI 参考](https://developers.openai.com/codex/cli/reference)
