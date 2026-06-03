# zmk-config-AroundFortyRB

Around Forty RBのファームウェアです。

## キー割り当て一覧

各レイヤーのキー割り当ては [KEYMAP.html](KEYMAP.html) にまとめています。ブラウザでレンダリング表示する場合は以下のリンクから閲覧できます。

https://htmlpreview.github.io/?https://github.com/ryo-aoki-pc/zmk-config-AroundFortyRB/blob/custom/KEYMAP.html

## Vial キーマップへの変換 (Keyboard Quantizer Mini)

このキーマップを [Keyboard Quantizer Mini](https://github.com/ryo-aoki-pc/vial-qmk-kq-mini)
(USB キーボードコンバーター) 上で再現するための Vial キーマップを、
[zmk-keymap-docgen の zmk_to_vial.py](https://github.com/ryo-aoki-pc/zmk-keymap-docgen)
で自動生成しています。

| ファイル | 用途 |
|---------|------|
| [KEYMAP.vil](KEYMAP.vil) | Vial GUI の `File → Load saved layout...` で読み込む (Quantizer Mini 接続状態で) |
| [KEYMAP-vial-report.md](KEYMAP-vial-report.md) | 変換内容のレポート (キー配置・マクロ・キーオーバーライド一覧) |
| `config/AroundForty-RB.vialmap.json` | 変換設定 (除外レイヤー・レイヤーキーの物理キー割当など) |

### レイヤーキーの割当 (US 配列)

BASE レイヤーでキーコードを持たないレイヤーキーは、接続したキーボードの以下のキーに割り当てています
(`config/AroundForty-RB.vialmap.json` で変更可能):

| ZMK | 接続キーボードのキー |
|-----|--------------------|
| `&mo SYM` (数字・記号レイヤー) | 右 Alt |
| `&mo VIM_BASE` (Vim ノーマルモード) | CapsLock |
| `&mo FUNC` (ファンクションレイヤー) | Menu / Application |
| `&mo BT` (Bluetooth レイヤー) | 割当なし (Quantizer では不要) |

### 再生成方法

```sh
# zmk-keymap-docgen をクローンした場所を指定して実行
python3 ../zmk-keymap-docgen/zmk_to_vial.py config/AroundForty-RB.keymap \
    -m config/AroundForty-RB.vialmap.json \
    --vil KEYMAP.vil \
    --report KEYMAP-vial-report.md \
    --inc ../vial-qmk-kq-mini/keyboards/sekigon/keyboard_quantizer/mini/keymaps/vial/zmk_keymap_defaults.inc
```

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
