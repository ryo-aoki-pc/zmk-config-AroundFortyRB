# zmk-config-AroundFortyRB

Around Forty RBのファームウェアです。

## キー割り当て一覧

各レイヤーのキー割り当ては [KEYMAP.html](KEYMAP.html) にまとめています。ブラウザでレンダリング表示する場合は以下のリンクから閲覧できます。

https://htmlpreview.github.io/?https://github.com/ryo-aoki-pc/zmk-config-AroundFortyRB/blob/custom/KEYMAP.html

## 命名規則（カスタムビヘイビア）

`config/AroundForty-RB.keymap` の Macro / Tap Dance / Mod Morph は以下の規則で命名します。

- **構造**：`<prefix>_vim_<id>` 形式。`<prefix>` は `macro_`（マクロ）/ `td_`（タップダンス）/ `mm_`（モッドモーフ）。ノードラベル・ノード名・`label` を一致させ、`label` はラベルの大文字にする（例：`mm_vim_g` → `label = "MM_VIM_G"`）。
- **Mod Morph の `<id>`**：キーに直接割り当てるモーフは無修飾時の vim キーで命名（`mm_vim_d` `mm_vim_g` など）。ベースが `&none`（修飾時のみ動作）またはネスト用ヘルパーは、修飾＋キーストロークで命名する（`mm_vim_shift_4` `mm_vim_ctrl_r` `mm_vim_shift_d`）。

-------------------------------------------------------------------------
mainブランチで実装済み
-------------------------------------------------------------------------

🟢Zmkfirmware v0.3に対応。（tsunoshuu様、PR感謝します）

🟢PMW3610のドライバを「badjeff/zmk-pmw3610-driver」に変更

🟢ZMK Studioに対応

🟢全角半角の切り替えマクロ：全角半角のトグルが一つのキーで可能

🟡Prospector Scannerの対応はいったん見送っています　/ ※Bluetooth接続が不安定になるため

以下、ご利用ガイドです。

https://note.com/razily/n/n0b3c5ff58d92

-------------------------------------------------------------------------
以下はmainブランチには未実装の開発版（dev-main）のみの機能です
-------------------------------------------------------------------------

🟢Slow Curor layer：カーソル速度を一時的に遅くて精密操作をしやすくします

🟢2種類のScroll Layer：上下左右のスクロールができるレイヤーと、縦限定スクロールができるレイヤーがあります
