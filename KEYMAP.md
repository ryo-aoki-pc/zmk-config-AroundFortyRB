# レイヤー キー割り当て一覧

- 各レイヤーごとに `## <LAYER>` セクションを設け、その中で「動作」「経路」の 2 ビューを並べる。
- 列ヘッダーは「キーラベル」と「バインディング (`&...`)」の 2 段表示。
- 各表の左端 1 列が「操作」（単発タップ / ダブルタップ / Shift+ / Ctrl+）。

## VIM_NORMAL_1

※ 42 個のバインディング位置。物理キーボード行ごとに 4 操作 × N キーの表で出力（QWERTY 配列）。

### 動作

#### Row 1 (QWERTY 上段)

| 操作 | Q<br>`&none` | W<br>`&kp LC(RIGHT)` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Ctrl+→ 入力 | Ctrl+→ 入力 | 何もしない | 何もしない | Ctrl+C 入力 | Ctrl+Z 入力 | 何もしない | END → ENTER | Ctrl+V 入力 |
| ダブルタップ | 何もしない | Ctrl+→ 入力 × 2 | Ctrl+→ 入力 × 2 | 何もしない | 何もしない | HOME → Shift+END → Ctrl+C | Ctrl+Z 入力 × 2 | 何もしない | END → ENTER（2 回実行） | Ctrl+V 入力 × 2 |
| Shift+ | 何もしない | Shift + Ctrl+→（OS で合成） | Shift + Ctrl+→（OS で合成） | 何もしない | 何もしない | Shift+END → Ctrl+C | Shift + Ctrl+Z（OS で合成） | 何もしない | HOME → ENTER → ↑ | Shift + Ctrl+V（OS で合成） |
| Ctrl+ | 何もしない | Ctrl + Ctrl+→（OS で合成） | Ctrl + Ctrl+→（OS で合成） | Ctrl+Y 入力 | 何もしない | Ctrl + Ctrl+C（OS で合成） | PAGE_UP 入力 | 何もしない | END → ENTER（Ctrl 物理保持で実行） | Ctrl + Ctrl+V（OS で合成） |

#### Row 2 (home row)

| 操作 | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | Left Ctrl 入力 | 何もしない | 何もしない | 何もしない | 何もしない | ← 入力 | ↓ 入力 | ↑ 入力 | → 入力 | Right Ctrl 入力 |
| ダブルタップ | Left Ctrl 入力 × 2 | 何もしない | HOME → Shift+END → Ctrl+X | 何もしない | Ctrl+HOME 入力 | ← 入力 × 2 | ↓ 入力 × 2 | ↑ 入力 × 2 | → 入力 × 2 | Right Ctrl 入力 × 2 |
| Shift+ | Shift + Left Ctrl（OS で合成） | 何もしない | Shift+END → Ctrl+X | 何もしない | Ctrl+END 入力 | Shift + ←（OS で合成） | END → DELETE → SPACE | Shift + ↑（OS で合成） | Shift + →（OS で合成） | Shift + Right Ctrl（OS で合成） |
| Ctrl+ | Ctrl + Left Ctrl（OS で合成） | 何もしない | PAGE_DOWN 入力 | 何もしない | 何もしない | Ctrl + ←（OS で合成） | Ctrl + ↓（OS で合成） | Ctrl + ↑（OS で合成） | Ctrl + →（OS で合成） | Ctrl + Right Ctrl（OS で合成） |

#### Row 3 (Z row)

| 操作 | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | Left Shift 入力 | DELETE 入力 | 何もしない | レイヤー 8 に切替 | Ctrl+← 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 |
| ダブルタップ | Left Shift 入力 × 2 | DELETE 入力 × 2 | 何もしない | レイヤー 8 に切替 | Ctrl+← 入力 × 2 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 × 2 |
| Shift+ | Shift + Left Shift（OS で合成） | Shift + DELETE（OS で合成） | 何もしない | HOME → Shift+↓ → レイヤー 8 へ | Shift + Ctrl+←（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Shift + Right Shift（OS で合成） |
| Ctrl+ | Ctrl + Left Shift（OS で合成） | Ctrl + DELETE（OS で合成） | 何もしない | レイヤー 8 に切替 | Ctrl + Ctrl+←（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + Right Shift（OS で合成） |

#### Row 4 (thumb)

| 操作 | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&mo 3` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | 何もしない | ENTER 入力（タップ） | 下位レイヤーの同位置にフォールスルー | 何もしない |
| ダブルタップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | 何もしない | ENTER 入力 × 2 | 下位レイヤーの同位置にフォールスルー | 何もしない |
| Shift+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | 何もしない | Shift + ENTER（ホールドでレイヤー 3） | 下位レイヤーの同位置にフォールスルー | 何もしない |
| Ctrl+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | レイヤー 3 を momentary（押下中のみ）有効化 | 何もしない | 何もしない | Ctrl + ENTER（ホールドでレイヤー 3） | 下位レイヤーの同位置にフォールスルー | 何もしない |

### 経路

#### Row 1 (QWERTY 上段)

| 操作 | Q<br>`&none` | W<br>`&kp LC(RIGHT)` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LC(RIGHT) | &kp LC(RIGHT) | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[0] → &kp LC(C) | mm_vim_ctrl_u[0] → &kp LC(Z) | &none | mm_vim_shift_o[0] → macro_vim_o | &kp LC(V) |
| ダブルタップ | &none | &kp LC(RIGHT)（tap-dance 未定義、連打） | &kp LC(RIGHT)（tap-dance 未定義、連打） | mm_vim_ctrl_r[0] → &none | &none | mm_vim_shift_y[0] → td_vim_y[1] → macro_vim_yy | mm_vim_ctrl_u[0] → &kp LC(Z)（tap-dance 未定義、連打） | &none | mm_vim_shift_o[0] → macro_vim_o（連打） | &kp LC(V)（tap-dance 未定義、連打） |
| Shift+ | &none | &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp LC(RIGHT)（物理 Shift は HID にそのまま伝わる） | mm_vim_ctrl_r[0] (Shift は本 mod-morph 検知外) → &none | &none | mm_vim_shift_y[1] (Shift 検知) → macro_vim_shift_y | mm_vim_ctrl_u[0] (Shift は本 mod-morph 検知外) → &kp LC(Z)（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_shift_o[1] (Shift 検知) → macro_vim_shift_o | &kp LC(V)（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &none | &kp LC(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | &kp LC(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_r[1] (Ctrl 検知) → &kp LC(Y) | &none | mm_vim_shift_y[0] (Ctrl は本 mod-morph 検知外) → td_vim_y[0] (tap-dance は mods 検知なし) → &kp LC(C)（物理 Ctrl は HID にそのまま伝わる） | mm_vim_ctrl_u[1] (Ctrl 検知) → &kp PAGE_UP | &none | mm_vim_shift_o[0] (Ctrl は本 mod-morph 検知外) → macro_vim_o | &kp LC(V)（物理 Ctrl は HID にそのまま伝わる） |

#### Row 2 (home row)

| 操作 | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | MINUS<br>`&kp RCTRL` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &kp LCTRL | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[0] → &none | &none | mm_vim_g[0] → td_vim_g[0] → &none | &kp LEFT | mm_vim_j[0] → &kp DOWN | &kp UP_ARROW | &kp RIGHT | &kp RCTRL |
| ダブルタップ | &kp LCTRL（tap-dance 未定義、連打） | &none | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[1] → macro_vim_dd | &none | mm_vim_g[0] → td_vim_g[1] → &kp LC(HOME) | &kp LEFT（tap-dance 未定義、連打） | mm_vim_j[0] → &kp DOWN（tap-dance 未定義、連打） | &kp UP_ARROW（tap-dance 未定義、連打） | &kp RIGHT（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） |
| Shift+ | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[0] (Shift は本 mod-morph 検知外) → mm_vim_shift_d[1] (Shift 検知) → macro_vim_shift_d | &none | mm_vim_g[1] (Shift 検知) → &kp LC(END) | &kp LEFT（物理 Shift は HID にそのまま伝わる） | mm_vim_j[1] (Shift 検知) → macro_vim_join | &kp UP_ARROW（物理 Shift は HID にそのまま伝わる） | &kp RIGHT（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_ctrl_then_shift_d[1] (Ctrl 検知) → &kp PAGE_DOWN | &none | mm_vim_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_g[0] (tap-dance は mods 検知なし) → &none | &kp LEFT（物理 Ctrl は HID にそのまま伝わる） | mm_vim_j[0] (Ctrl は本 mod-morph 検知外) → &kp DOWN（物理 Ctrl は HID にそのまま伝わる） | &kp UP_ARROW（物理 Ctrl は HID にそのまま伝わる） | &kp RIGHT（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） |

#### Row 3 (Z row)

| 操作 | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &kp LEFT_SHIFT | &kp DELETE | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT) | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT |
| ダブルタップ | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &kp DELETE（tap-dance 未定義、連打） | &none | mm_vim_v[0] → &to 8 | &kp LC(LEFT)（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） |
| Shift+ | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &kp DELETE（物理 Shift は HID にそのまま伝わる） | &none | mm_vim_v[1] (Shift 検知) → macro_vim_v_line | &kp LC(LEFT)（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &kp DELETE（物理 Ctrl は HID にそのまま伝わる） | &none | mm_vim_v[0] (Ctrl は本 mod-morph 検知外) → &to 8 | &kp LC(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） |

#### Row 4 (thumb)

| 操作 | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&mo 3` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &trans | &trans | &none | &none | &mo 3 | &none | &none | &lt 3 ENTER | &trans | &none |
| ダブルタップ | &none | &trans | &trans | &none | &none | &mo 3 | &none | &none | &lt 3 ENTER（連打） | &trans | &none |
| Shift+ | &none | &trans | &trans | &none | &none | &mo 3 | &none | &none | &lt 3 ENTER | &trans | &none |
| Ctrl+ | &none | &trans | &trans | &none | &none | &mo 3 | &none | &none | &lt 3 ENTER | &trans | &none |

## VIM_NORMAL_2

※ 42 個のバインディング位置。物理キーボード行ごとに 4 操作 × N キーの表で出力（QWERTY 配列）。

### 動作

#### Row 1 (QWERTY 上段)

| 操作 | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | HOME 入力 |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | HOME 入力 × 2 |
| Shift+ | 何もしない | 何もしない | 何もしない | END 入力 | 何もしない | HOME 入力 | 何もしない | 何もしない | 何もしない | Shift + HOME（OS で合成） |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + HOME（OS で合成） |

#### Row 2 (home row)

| 操作 | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&none` | MINUS<br>`&kp RCTRL` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | Left Ctrl 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Ctrl 入力 |
| ダブルタップ | Left Ctrl 入力 × 2 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Ctrl 入力 × 2 |
| Shift+ | Shift + Left Ctrl（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Shift + Right Ctrl（OS で合成） |
| Ctrl+ | Ctrl + Left Ctrl（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + Right Ctrl（OS で合成） |

#### Row 3 (Z row)

| 操作 | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | Left Shift 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 |
| ダブルタップ | Left Shift 入力 × 2 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 × 2 |
| Shift+ | Shift + Left Shift（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Shift + Right Shift（OS で合成） |
| Ctrl+ | Ctrl + Left Shift（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + Right Shift（OS で合成） |

#### Row 4 (thumb)

| 操作 | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&trans` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない |
| ダブルタップ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない |
| Shift+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない |
| Ctrl+ | 何もしない | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 下位レイヤーの同位置にフォールスルー | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | 下位レイヤーの同位置にフォールスルー | 何もしない |

### 経路

#### Row 1 (QWERTY 上段)

| 操作 | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | mm_vim_shift_4[0] → &none | &none | mm_vim_shift_6[0] → &none | &none | &none | &none | &kp HOME |
| ダブルタップ | &none | &none | &none | mm_vim_shift_4[0] → &none | &none | mm_vim_shift_6[0] → &none | &none | &none | &none | &kp HOME（tap-dance 未定義、連打） |
| Shift+ | &none | &none | &none | mm_vim_shift_4[1] (Shift 検知) → &kp END | &none | mm_vim_shift_6[1] (Shift 検知) → &kp HOME | &none | &none | &none | &kp HOME（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &none | &none | &none | mm_vim_shift_4[0] (Ctrl は本 mod-morph 検知外) → &none | &none | mm_vim_shift_6[0] (Ctrl は本 mod-morph 検知外) → &none | &none | &none | &none | &kp HOME（物理 Ctrl は HID にそのまま伝わる） |

#### Row 2 (home row)

| 操作 | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&none` | MINUS<br>`&kp RCTRL` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &kp LCTRL | &none | &none | &none | &none | &none | &none | &none | &none | &kp RCTRL |
| ダブルタップ | &kp LCTRL（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | &none | &none | &kp RCTRL（tap-dance 未定義、連打） |
| Shift+ | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &none | &none | &kp RCTRL（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &none | &none | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） |

#### Row 3 (Z row)

| 操作 | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &kp LEFT_SHIFT | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT |
| ダブルタップ | &kp LEFT_SHIFT（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） |
| Shift+ | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） |

#### Row 4 (thumb)

| 操作 | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&trans` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &trans | &none |
| ダブルタップ | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &trans | &none |
| Shift+ | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &trans | &none |
| Ctrl+ | &none | &trans | &trans | &trans | &none | &none | &none | &none | &none | &trans | &none |

## VIM_VISUAL

※ 42 個のバインディング位置。物理キーボード行ごとに 4 操作 × N キーの表で出力（QWERTY 配列）。

### 動作

#### Row 1 (QWERTY 上段)

| 操作 | Q<br>`&none` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&macro_vim_visual_y` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | Shift+Ctrl+→ 入力 | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ |
| ダブルタップ | 何もしない | Shift+Ctrl+→ 入力 × 2 | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（2 回実行） | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（2 回実行） |
| Shift+ | 何もしない | Shift + Shift+Ctrl+→（OS で合成） | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（Shift 物理保持で実行） |
| Ctrl+ | 何もしない | Ctrl + Shift+Ctrl+→（OS で合成） | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+C → → → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+V → レイヤー 0 へ（Ctrl 物理保持で実行） |

#### Row 2 (home row)

| 操作 | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | Left Ctrl 入力 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | 何もしない | 何もしない | Shift+← 入力 | Shift+↓ 入力 | Shift+UP 入力 | Shift+→ 入力 | Right Ctrl 入力 |
| ダブルタップ | Left Ctrl 入力 × 2 | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | 何もしない | Shift+Ctrl+HOME 入力 | Shift+← 入力 × 2 | Shift+↓ 入力 × 2 | Shift+UP 入力 × 2 | Shift+→ 入力 × 2 | Right Ctrl 入力 × 2 |
| Shift+ | Shift + Left Ctrl（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | Shift+Ctrl+END 入力 | Shift + Shift+←（OS で合成） | Shift + Shift+↓（OS で合成） | Shift + Shift+UP（OS で合成） | Shift + Shift+→（OS で合成） | Shift + Right Ctrl（OS で合成） |
| Ctrl+ | Ctrl + Left Ctrl（OS で合成） | 何もしない | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | 何もしない | Ctrl + Shift+←（OS で合成） | Ctrl + Shift+↓（OS で合成） | Ctrl + Shift+UP（OS で合成） | Ctrl + Shift+→（OS で合成） | Ctrl + Right Ctrl（OS で合成） |

#### Row 3 (Z row)

| 操作 | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&macro_vim_visual_cut` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | Left Shift 入力 | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Shift+Ctrl+← 入力 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 |
| ダブルタップ | Left Shift 入力 × 2 | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Shift+Ctrl+← 入力 × 2 | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Right Shift 入力 × 2 |
| Shift+ | Shift + Left Shift（OS で合成） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Shift + Shift+Ctrl+←（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Shift + Right Shift（OS で合成） |
| Ctrl+ | Ctrl + Left Shift（OS で合成） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → Ctrl+X → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Ctrl + Shift+Ctrl+←（OS で合成） | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Ctrl + Right Shift（OS で合成） |

#### Row 4 (thumb)

| 操作 | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&macro_vim_visual_exit` | mo2<br>`&macro_vim_visual_exit` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&macro_vim_visual_exit` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ | 何もしない | 何もしない |
| ダブルタップ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（2 回実行） | 何もしない | 何もしない |
| Shift+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Shift 物理保持で実行） | 何もしない | 何もしない |
| Ctrl+ | 何もしない | 何もしない | 何もしない | 何もしない | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | Left Shift 解放 → Right Shift 解放 → → → レイヤー 0 へ（Ctrl 物理保持で実行） | 何もしない | 何もしない |

### 経路

#### Row 1 (QWERTY 上段)

| 操作 | Q<br>`&none` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&macro_vim_visual_y` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &kp LS(LC(RIGHT)) | &none | &none | &none | macro_vim_visual_y | &none | &none | &none | macro_vim_visual_p |
| ダブルタップ | &none | &kp LS(LC(RIGHT))（tap-dance 未定義、連打） | &none | &none | &none | macro_vim_visual_y（連打） | &none | &none | &none | macro_vim_visual_p（連打） |
| Shift+ | &none | &kp LS(LC(RIGHT))（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | macro_vim_visual_y | &none | &none | &none | macro_vim_visual_p |
| Ctrl+ | &none | &kp LS(LC(RIGHT))（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | macro_vim_visual_y | &none | &none | &none | macro_vim_visual_p |

#### Row 2 (home row)

| 操作 | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | MINUS<br>`&kp RCTRL` |
|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &kp LCTRL | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] → td_vim_visual_g[0] → &none | &kp LS(LEFT) | &kp LS(DOWN) | &kp LS(UP) | &kp LS(RIGHT) | &kp RCTRL |
| ダブルタップ | &kp LCTRL（tap-dance 未定義、連打） | &none | macro_vim_visual_cut（連打） | &none | mm_vim_visual_g[0] → td_vim_visual_g[1] → &kp LS(LC(HOME)) | &kp LS(LEFT)（tap-dance 未定義、連打） | &kp LS(DOWN)（tap-dance 未定義、連打） | &kp LS(UP)（tap-dance 未定義、連打） | &kp LS(RIGHT)（tap-dance 未定義、連打） | &kp RCTRL（tap-dance 未定義、連打） |
| Shift+ | &kp LCTRL（物理 Shift は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[1] (Shift 検知) → &kp LS(LC(END)) | &kp LS(LEFT)（物理 Shift は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Shift は HID にそのまま伝わる） | &kp LS(UP)（物理 Shift は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Shift は HID にそのまま伝わる） | &kp RCTRL（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &kp LCTRL（物理 Ctrl は HID にそのまま伝わる） | &none | macro_vim_visual_cut | &none | mm_vim_visual_g[0] (Ctrl は本 mod-morph 検知外) → td_vim_visual_g[0] (tap-dance は mods 検知なし) → &none | &kp LS(LEFT)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(DOWN)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(UP)（物理 Ctrl は HID にそのまま伝わる） | &kp LS(RIGHT)（物理 Ctrl は HID にそのまま伝わる） | &kp RCTRL（物理 Ctrl は HID にそのまま伝わる） |

#### Row 3 (Z row)

| 操作 | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&macro_vim_visual_cut` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | COMMA<br>`&none` | PERIOD<br>`&none` | SLASH<br>`&kp RIGHT_SHIFT` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &kp LEFT_SHIFT | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT)) | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT |
| ダブルタップ | &kp LEFT_SHIFT（tap-dance 未定義、連打） | macro_vim_visual_cut（連打） | macro_vim_visual_cut（連打） | macro_vim_visual_exit（連打） | &kp LS(LC(LEFT))（tap-dance 未定義、連打） | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（tap-dance 未定義、連打） |
| Shift+ | &kp LEFT_SHIFT（物理 Shift は HID にそのまま伝わる） | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Shift は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Shift は HID にそのまま伝わる） |
| Ctrl+ | &kp LEFT_SHIFT（物理 Ctrl は HID にそのまま伝わる） | macro_vim_visual_cut | macro_vim_visual_cut | macro_vim_visual_exit | &kp LS(LC(LEFT))（物理 Ctrl は HID にそのまま伝わる） | &none | &none | &none | &none | &none | &kp RIGHT_SHIFT（物理 Ctrl は HID にそのまま伝わる） |

#### Row 4 (thumb)

| 操作 | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&macro_vim_visual_exit` | mo2<br>`&macro_vim_visual_exit` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&macro_vim_visual_exit` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 単発タップ | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | &none | macro_vim_visual_exit | &none | &none |
| ダブルタップ | &none | &none | &none | &none | &none | macro_vim_visual_exit（連打） | macro_vim_visual_exit（連打） | &none | macro_vim_visual_exit（連打） | &none | &none |
| Shift+ | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | &none | macro_vim_visual_exit | &none | &none |
| Ctrl+ | &none | &none | &none | &none | &none | macro_vim_visual_exit | macro_vim_visual_exit | &none | macro_vim_visual_exit | &none | &none |

