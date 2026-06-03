# ZMK → Vial 変換レポート

- 変換元: `AroundForty-RB.keymap`
- 変換先: sekigon/keyboard_quantizer/mini

## レイヤー対応

| ZMK レイヤー | 別名 | Vial レイヤー |
|---|---|---|
| BASE_QWERTY | BASE | 0 |
| NUM_SYMBOL | SYM | 1 |
| VIM_NORMAL_BASE | VIM_BASE | 2 |
| VIM_NORMAL_SYM | VIM_SYM | 3 |
| VIM_VISUAL_BASE | VIM_VISUAL | 4 |
| VIM_VISUAL_SYM | VIM_VIS_SYM | 5 |
| FUNCTION | FUNC | 6 |
| BLUETOOTH | BT | (除外) |
| MOUSE_MOVE | MOUS | (除外) |
| MOUSE_SCROLL | SCRL | (除外) |

## キー配置 (BASE レイヤーのアイデンティティ → Quantizer 行列位置)

| ZMK位置 | アイデンティティ | 行列 (row, col) |
|---|---|---|
| 0 | `&kp Q` | (3, 4) |
| 1 | `&kp W` | (4, 2) |
| 2 | `&kp E` | (2, 0) |
| 3 | `&kp R` | (3, 5) |
| 4 | `&kp T` | (3, 7) |
| 5 | `&kp Y` | (4, 4) |
| 6 | `&kp U` | (4, 0) |
| 7 | `&kp I` | (2, 4) |
| 8 | `&kp O` | (3, 2) |
| 9 | `&kp P` | (3, 3) |
| 10 | `&mt LEFT_CONTROL A` | (1, 4) |
| 11 | `&kp S` | (3, 6) |
| 12 | `&kp D` | (1, 7) |
| 13 | `&kp F` | (2, 1) |
| 14 | `&kp G` | (2, 2) |
| 15 | `&kp H` | (2, 3) |
| 16 | `&kp J` | (2, 5) |
| 17 | `&kp K` | (2, 6) |
| 18 | `&kp L` | (2, 7) |
| 19 | `&mt RCTRL MINUS` | (6, 5) |
| 20 | `&mt LEFT_SHIFT Z` | (4, 5) |
| 21 | `&kp X` | (4, 3) |
| 22 | `&kp C` | (1, 6) |
| 23 | `&kp V` | (4, 1) |
| 24 | `&kp B` | (1, 5) |
| 25 | `&mo 7 (マップ対象外)` | — |
| 26 | `&kp N` | (3, 1) |
| 27 | `&kp M` | (3, 0) |
| 28 | `&kp COMMA` | (7, 6) |
| 29 | `&kp PERIOD` | (7, 7) |
| 30 | `&mt RIGHT_SHIFT SLASH` | (8, 0) |
| 31 | `&mo 6 → KC_APPLICATION (設定による割当)` | (13, 5) |
| 32 | `&kp LEFT_WIN` | (0, 3) |
| 33 | `&kp LEFT_ALT` | (0, 2) |
| 34 | `&lt 2 SPACE` | (6, 4) |
| 35 | `&lt 2 SPACE` | (6, 4) |
| 36 | `&mo 1 → KC_RIGHT_ALT (設定による割当)` | (0, 6) |
| 37 | `&lt 1 ENTER` | (6, 0) |
| 38 | `&mo 7 (マップ対象外)` | — |
| 39 | `&mo 2 → KC_CAPS_LOCK (設定による割当)` | (8, 1) |
| 40 | `&mo 6 → KC_APPLICATION (設定による割当)` | (13, 5) |
| 41 | `&mo 6 → KC_APPLICATION (設定による割当)` | (13, 5) |

## マクロ

| Vial | ZMK マクロ | アクション |
|---|---|---|
| M0 | macro_vim_dd | tap KC_HOME → delay 100ms → down KC_LEFT_SHIFT → tap KC_END → up KC_LEFT_SHIFT → delay 100ms → down KC_LEFT_CTRL → tap KC_X → up KC_LEFT_CTRL |
| M1 | macro_vim_yy | tap KC_HOME → delay 100ms → down KC_LEFT_SHIFT → tap KC_END → up KC_LEFT_SHIFT → delay 100ms → down KC_LEFT_CTRL → tap KC_C → up KC_LEFT_CTRL |
| M2 | macro_vim_shift_d | down KC_LEFT_SHIFT → tap KC_END → up KC_LEFT_SHIFT → delay 100ms → down KC_LEFT_CTRL → tap KC_X → up KC_LEFT_CTRL |
| M3 | macro_vim_shift_y | down KC_LEFT_SHIFT → tap KC_END → up KC_LEFT_SHIFT → delay 100ms → down KC_LEFT_CTRL → tap KC_C → up KC_LEFT_CTRL |
| M4 | macro_vim_o | tap KC_END → delay 100ms → tap KC_ENTER |
| M5 | macro_vim_shift_o | tap KC_HOME → delay 100ms → tap KC_ENTER → delay 100ms → tap KC_UP |
| M6 | macro_vim_join | tap KC_END → delay 100ms → tap KC_DELETE → delay 100ms → tap KC_SPACE |
| M7 | macro_vim_visual_y | up KC_LEFT_SHIFT, KC_RIGHT_SHIFT → down KC_LEFT_CTRL → tap KC_C → up KC_LEFT_CTRL → delay 50ms → tap KC_RIGHT → delay 50ms → tap TO(0) |
| M8 | macro_vim_visual_cut | up KC_LEFT_SHIFT, KC_RIGHT_SHIFT → down KC_LEFT_CTRL → tap KC_X → up KC_LEFT_CTRL → delay 50ms → tap TO(0) |
| M9 | macro_vim_visual_p | up KC_LEFT_SHIFT, KC_RIGHT_SHIFT → down KC_LEFT_CTRL → tap KC_V → up KC_LEFT_CTRL → delay 50ms → tap TO(0) |
| M10 | macro_vim_v_line | tap KC_HOME → delay 50ms → down KC_LEFT_SHIFT → tap KC_DOWN → up KC_LEFT_SHIFT → delay 50ms → tap TO(4) |
| M11 | macro_vim_visual_exit | up KC_LEFT_SHIFT, KC_RIGHT_SHIFT → tap KC_RIGHT → delay 50ms → tap TO(0) |

## タップダンス

| Vial | ZMK | 1打 | 2打 | term |
|---|---|---|---|---|
| TD(0) | td_vim_d | KC_NO | QK_MACRO_0 | 150ms |
| TD(1) | td_vim_y | KC_NO | QK_MACRO_1 | 150ms |
| TD(2) | td_vim_g | KC_NO | LCTL(KC_HOME) | 150ms |
| TD(3) | td_vim_visual_g | KC_NO | LSFT(LCTL(KC_HOME)) | 150ms |

## キーオーバーライド (モッドモーフ変換)

| # | 元モーフ | トリガー | 条件 | 置換 | レイヤー |
|---|---|---|---|---|---|
| 0 | mm_vim_w | QK_KB_3 | LCtrl+RCtrl 非押下時 | LCTL(KC_RIGHT) | 2 |
| 1 | mm_vim_w | QK_KB_3 | LCtrl+RCtrl 押下時 | LCTL(KC_BACKSPACE) | 2 |
| 2 | mm_vim_ctrl_r | QK_KB_4 | LCtrl+RCtrl 押下時 | LCTL(KC_Y) | 2 |
| 3 | mm_vim_y | TD(1) | LShift+RShift 押下時 | QK_MACRO_3 | 2 |
| 4 | mm_vim_u | QK_KB_5 | LCtrl+RCtrl 非押下時 | LCTL(KC_Z) | 2 |
| 5 | mm_vim_u | QK_KB_5 | LCtrl+RCtrl 押下時 | KC_PAGE_UP | 2 |
| 6 | mm_vim_o | QK_KB_6 | LShift+RShift 非押下時 | QK_MACRO_4 | 2 |
| 7 | mm_vim_o | QK_KB_6 | LShift+RShift 押下時 | QK_MACRO_5 | 2 |
| 8 | mm_vim_shift_d | TD(0) | LShift+RShift 押下時 | QK_MACRO_2 | 2 |
| 9 | mm_vim_d | TD(0) | LCtrl+RCtrl 押下時 | KC_PAGE_DOWN | 2 |
| 10 | mm_vim_g | TD(2) | LShift+RShift 押下時 | LCTL(KC_END) | 2 |
| 11 | mm_vim_j | KC_DOWN | LShift+RShift 押下時 | QK_MACRO_6 | 2 |
| 12 | mm_vim_v | TO(4) | LShift+RShift 押下時 | QK_MACRO_10 | 2 |
| 13 | mm_vim_shift_4 | QK_KB_7 | LShift+RShift 押下時 | KC_END | 3 |
| 14 | mm_vim_shift_6 | QK_KB_8 | LShift+RShift 押下時 | KC_HOME | 3 |
| 15 | mm_vim_visual_g | TD(3) | LShift+RShift 押下時 | LSFT(LCTL(KC_END)) | 4 |
| 16 | mm_vim_visual_shift_4 | QK_KB_9 | LShift+RShift 押下時 | LSFT(KC_END) | 5 |
| 17 | mm_vim_visual_shift_6 | QK_KB_10 | LShift+RShift 押下時 | LSFT(KC_HOME) | 5 |

## キャリアキーコード割当

モッドモーフの無修飾側がトリガーにできないキーコード (&none / 修飾付き / マクロ) の場合、
カスタムキーコード (QK_KB_n) を「キャリア」としてキー位置に配置しています。

| キーコード | 元モーフ | 理由 |
|---|---|---|
| QK_KB_3 | mm_vim_w | 無修飾側が修飾付きキーコード |
| QK_KB_4 | mm_vim_ctrl_r | 無修飾側が &none |
| QK_KB_5 | mm_vim_u | 無修飾側が修飾付きキーコード |
| QK_KB_6 | mm_vim_o | 無修飾側がマクロ |
| QK_KB_7 | mm_vim_shift_4 | 無修飾側が &none |
| QK_KB_8 | mm_vim_shift_6 | 無修飾側が &none |
| QK_KB_9 | mm_vim_visual_shift_4 | 無修飾側が &none |
| QK_KB_10 | mm_vim_visual_shift_6 | 無修飾側が &none |

### vial.json customKeycodes 追記用スニペット

これらのキャリアはファームウェアの `vial.json` の `customKeycodes` で定義が必要です。
未定義のファームウェアでは Vial GUI がキャリアを解決できず、`.vil` の
キーオーバーライド取り込み時にクラッシュします (`argument of type 'int' is not iterable`)。以下を `customKeycodes` 配列に追記してください (既存の3エントリの後ろに):

```json
[
  {
    "name": "MM_VIM_W",
    "title": "ZMK mod-morph carrier: mm_vim_w",
    "shortName": "ZMK\n3"
  },
  {
    "name": "MM_VIM_CTRL_R",
    "title": "ZMK mod-morph carrier: mm_vim_ctrl_r",
    "shortName": "ZMK\n4"
  },
  {
    "name": "MM_VIM_U",
    "title": "ZMK mod-morph carrier: mm_vim_u",
    "shortName": "ZMK\n5"
  },
  {
    "name": "MM_VIM_O",
    "title": "ZMK mod-morph carrier: mm_vim_o",
    "shortName": "ZMK\n6"
  },
  {
    "name": "MM_VIM_SHIFT_4",
    "title": "ZMK mod-morph carrier: mm_vim_shift_4",
    "shortName": "ZMK\n7"
  },
  {
    "name": "MM_VIM_SHIFT_6",
    "title": "ZMK mod-morph carrier: mm_vim_shift_6",
    "shortName": "ZMK\n8"
  },
  {
    "name": "MM_VIM_VISUAL_SHIFT_4",
    "title": "ZMK mod-morph carrier: mm_vim_visual_shift_4",
    "shortName": "ZMK\n9"
  },
  {
    "name": "MM_VIM_VISUAL_SHIFT_6",
    "title": "ZMK mod-morph carrier: mm_vim_visual_shift_6",
    "shortName": "ZMK\n10"
  }
]
```

## リソース使用量

| リソース | 使用 | 上限 |
|---|---|---|
| レイヤー | 7 | 8 |
| マクロ | 12 | 16 |
| タップダンス | 4 | 32 |
| キーオーバーライド | 18 | 32 |
| カスタムキーコード | 8 (QK_KB_3〜) | 32 |

## 使い方

### 方法A: ファームウェア組込 (推奨・確実)

生成された `.inc` を vial-qmk の
`keyboards/sekigon/keyboard_quantizer/mini/keymaps/vial/` に配置し、keymap.c に組み込みます
(`.inc` 冒頭のコメント参照: ① `void zmk_keymap_apply_if_outdated(void);` を前方宣言、
② `keyboard_post_init_user()` の末尾で呼び出し、③ ファイル末尾で `#include`)。

**ビルドして書き込むだけで**、レイヤー・マクロ・タップダンス・**キーオーバーライド**を
含む全設定が次回起動時に EEPROM へ自動適用されます (キーマップ内容のハッシュを保存し、
変更を検出したときだけ適用するため、その後の Vial 編集は保持されます)。
vial-gui の取り込み経路を通らないため、GUI のバージョン差異の影響も受けません。

### 方法B: Vial GUI で .vil を読み込む

`File → Load saved layout...` で生成された `.vil` を読み込みます
(Quantizer Mini を接続した状態で)。
レイヤー・マクロ・タップダンス・キーオーバーライドが書き込まれます。
