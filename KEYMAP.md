# キー割り当て一覧

※ 3 個のレイヤーのキー割り当てを 1 ファイルに集約。各レイヤー 42 バインディング位置を「動作」セクションでまとめてから「経路」セクションに進む。

- 各 row セクション行に「キーラベル」と「バインディング (`&...`)」の 2 段表示でキー位置を示す。
- 各表の左端 1 列が「操作」（単発タップ / ホールド / ダブルタップ / Shift+ / Ctrl+）または「■ Row N」見出し。

## 動作

### DEFAULT レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&kp Q` | W<br>`&kp W` | E<br>`&kp E` | R<br>`&kp R` | T<br>`&kp T` | Y<br>`&kp Y` | U<br>`&kp U` | I<br>`&kp I` | O<br>`&kp O` | P<br>`&kp P` |
| 単発タップ | Q | W | E | R | T | Y | U | I | O | P |
| ■ Row 2 (home row) | A<br>`&mt LEFT_CONTROL A` | S<br>`&kp S` | D<br>`&kp D` | F<br>`&kp F` | G<br>`&kp G` | H<br>`&kp H` | J<br>`&kp J` | K<br>`&kp K` | L<br>`&kp L` | -<br>`&mt RCTRL MINUS` |
| 単発タップ | A | S | D | F | G | H | J | K | L | - |
| ホールド | LCtrl | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | RCtrl |
| ■ Row 3 (Z row) | Z<br>`&mt LEFT_SHIFT Z` | X<br>`&kp X` | C<br>`&kp C` | V<br>`&kp V` | B<br>`&kp B` | N<br>`&kp N` | M<br>`&kp M` | ,<br>`&kp COMMA` | .<br>`&kp PERIOD` | /<br>`&mt RIGHT_SHIFT SLASH` |
| 単発タップ | Z | X | C | V | B | N | M | , | . | / |
| ホールド | LShift | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | RShift |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&mo 6` | LEFT_WIN<br>`&kp LEFT_WIN` | LEFT_ALT<br>`&kp LEFT_ALT` | lt2 SPACE<br>`&lt 2 SPACE` | lt2 SPACE<br>`&lt 2 SPACE` | mo1 (L center)<br>`&mo 1` | mo2<br>`&lt 1 ENTER` | lt1 ENTER<br>`&mo 2` | mo6 (R)<br>`&mo 6` | mo6 (R outer)<br>`&mo 6` |
| 単発タップ | L6 | LWin | LAlt | SPACE | SPACE | L1 | ENTER | L2 | L6 | L6 |
| ホールド | 〃 | 〃 | 〃 | L2 | L2 | 〃 | L1 | 〃 | 〃 | 〃 |

### SYMBOL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&kp N1` | W<br>`&kp N2` | E<br>`&kp N3` | R<br>`&kp N4` | T<br>`&kp N5` | Y<br>`&kp N6` | U<br>`&kp N7` | I<br>`&kp N8` | O<br>`&kp N9` | P<br>`&kp N0` |
| 単発タップ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
| ■ Row 2 (home row) | A<br>`&mt LCTRL TAB` | S<br>`&kp GRAVE` | D<br>`&kp LEFT_BRACKET` | F<br>`&kp RIGHT_BRACKET` | G<br>`&kp DELETE` | H<br>`&kp BACKSPACE` | J<br>`&kp SEMICOLON` | K<br>`&kp SINGLE_QUOTE` | L<br>`&kp BACKSLASH` | -<br>`&trans` |
| 単発タップ | TAB | &#96; | [ | ] | DEL | BS | ; | ' | &#92; | ▽ |
| ホールド | LCtrl | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| ■ Row 3 (Z row) | Z<br>`&mt LEFT_SHIFT ESCAPE` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&kp EQUAL` | ,<br>`&trans` | .<br>`&trans` | /<br>`&trans` |
| 単発タップ | ESC |  |  |  |  |  | = | ▽ | ▽ | ▽ |
| ホールド | LShift |  |  |  |  |  | 〃 | 〃 | 〃 | 〃 |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&lt 3 SPACE` | lt2 SPACE<br>`&lt 3 SPACE` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&mo 3` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ | SPACE | SPACE |  |  | L3 | ▽ |  |
| ホールド |  | 〃 | 〃 | L3 | L3 |  |  | 〃 | 〃 |  |

### VIM_NORMAL_1 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` |
| 単発タップ |  | Ctrl+→ | Ctrl+→ |  |  |  | Ctrl+Z |  | END ▸ ENTER | Ctrl+V |
| ダブルタップ |  | 〃 | 〃 |  |  | HOME ▸ Shift+END ▸ Ctrl+C | 〃 |  | 〃 | 〃 |
| Shift+ |  | 〃 | 〃 |  |  | Shift+END ▸ Ctrl+C | 〃 |  | HOME ▸ ENTER ▸ ↑ | 〃 |
| Ctrl+ |  | Ctrl+BS | 〃 | Ctrl+Y |  |  | PgUp |  | 〃 | 〃 |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | -<br>`&kp RCTRL` |
| 単発タップ | LCtrl |  |  |  |  | ← | ↓ | ↑ | → | RCtrl |
| ダブルタップ | 〃 |  | HOME ▸ Shift+END ▸ Ctrl+X |  | Ctrl+HOME | 〃 | 〃 | 〃 | 〃 | 〃 |
| Shift+ | 〃 |  | Shift+END ▸ Ctrl+X |  | Ctrl+END | 〃 | END ▸ DEL ▸ SPACE | 〃 | 〃 | 〃 |
| Ctrl+ | 〃 |  | PgDn |  |  | 〃 | 〃 | 〃 | 〃 | 〃 |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | N<br>`&mm_vim_n` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | LShift | DEL |  | ⇒L8 | Ctrl+← | F3 |  |  |  | RShift |
| Shift+ | 〃 | 〃 |  | HOME ▸ Shift+↓ ▸ レイヤー 8 へ | 〃 | Shift+F3 |  |  |  | 〃 |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&mo 3` | mo2<br>`&lt 3 ENTER` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  | L3 | ENTER |  | ▽ |  |
| ホールド |  | 〃 | 〃 |  |  | 〃 | L3 |  | 〃 |  |

### VIM_NORMAL_2 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` |
| 単発タップ |  |  |  |  |  |  |  |  |  | HOME |
| Shift+ |  |  |  | END |  | HOME |  |  |  | 〃 |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&kp LEFT` | J<br>`&none` | K<br>`&none` | L<br>`&none` | -<br>`&kp RCTRL` |
| 単発タップ | LCtrl |  |  |  |  | ← |  |  |  | RCtrl |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | LShift |  |  |  |  |  |  |  |  | RShift |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  |  |  |  | ▽ |  |

### MOUSE レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 2 (home row) | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&mo 5` | L<br>`&none` | -<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  | L5 |  |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### SCROLL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 2 (home row) | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&mkp MB1` | K<br>`&none` | L<br>`&mkp MB2` | -<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&mkp MB4` | ,<br>`&none` | .<br>`&mkp MB5` | /<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### FUNCTION レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&kp F1` | W<br>`&kp F2` | E<br>`&kp F3` | R<br>`&kp F4` | T<br>`&kp F5` | Y<br>`&kp F6` | U<br>`&kp F7` | I<br>`&kp F8` | O<br>`&kp F9` | P<br>`&kp F10` |
| 単発タップ | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 |
| ■ Row 2 (home row) | A<br>`&none` | S<br>`&sys_reset` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&sys_reset` | -<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&bootloader` | N<br>`&bootloader` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### BLUETOOTH レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&bt BT_SEL 0` | W<br>`&bt BT_SEL 1` | E<br>`&bt BT_SEL 2` | R<br>`&bt BT_SEL 3` | T<br>`&bt BT_SEL 4` | Y<br>`&none` | U<br>`&out OUT_USB` | I<br>`&none` | O<br>`&none` | P<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 2 (home row) | A<br>`&bt BT_CLR_ALL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&none` | -<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&bt BT_CLR` | V<br>`&none` | B<br>`&out OUT_BLE` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### VIM_VISUAL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` |
| 単発タップ |  | Shift+Ctrl+→ | Shift+Ctrl+→ |  |  |  |  |  |  | LShift ▸ RShift ▸ Ctrl+V ▸ レイヤー 0 へ |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | -<br>`&kp RCTRL` |
| 単発タップ | LCtrl |  | LShift ▸ RShift ▸ Ctrl+X ▸ レイヤー 0 へ |  |  | Shift+← | Shift+↓ | Shift+↑ | Shift+→ | RCtrl |
| ダブルタップ | 〃 |  | 〃 |  | Shift+Ctrl+HOME | 〃 | 〃 | 〃 | 〃 | 〃 |
| Shift+ | 〃 |  | 〃 |  | Shift+Ctrl+END | 〃 | 〃 | 〃 | 〃 | 〃 |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&none` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | N<br>`&kp F3` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | LShift | LShift ▸ RShift ▸ Ctrl+X ▸ レイヤー 0 へ |  | LShift ▸ RShift ▸ → ▸ レイヤー 0 へ | Shift+Ctrl+← | F3 |  |  |  | RShift |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

## 経路

### DEFAULT レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&kp Q` | W<br>`&kp W` | E<br>`&kp E` | R<br>`&kp R` | T<br>`&kp T` | Y<br>`&kp Y` | U<br>`&kp U` | I<br>`&kp I` | O<br>`&kp O` | P<br>`&kp P` |
| 単発タップ | &kp Q | &kp W | &kp E | &kp R | &kp T | &kp Y | &kp U | &kp I | &kp O | &kp P |
| ■ Row 2 (home row) | A<br>`&mt LEFT_CONTROL A` | S<br>`&kp S` | D<br>`&kp D` | F<br>`&kp F` | G<br>`&kp G` | H<br>`&kp H` | J<br>`&kp J` | K<br>`&kp K` | L<br>`&kp L` | -<br>`&mt RCTRL MINUS` |
| 単発タップ | &mt LEFT_CONTROL A | &kp S | &kp D | &kp F | &kp G | &kp H | &kp J | &kp K | &kp L | &mt RCTRL MINUS |
| ホールド | &mt LEFT_CONTROL A | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | &mt RCTRL MINUS |
| ■ Row 3 (Z row) | Z<br>`&mt LEFT_SHIFT Z` | X<br>`&kp X` | C<br>`&kp C` | V<br>`&kp V` | B<br>`&kp B` | N<br>`&kp N` | M<br>`&kp M` | ,<br>`&kp COMMA` | .<br>`&kp PERIOD` | /<br>`&mt RIGHT_SHIFT SLASH` |
| 単発タップ | &mt LEFT_SHIFT Z | &kp X | &kp C | &kp V | &kp B | &kp N | &kp M | &kp COMMA | &kp PERIOD | &mt RIGHT_SHIFT SLASH |
| ホールド | &mt LEFT_SHIFT Z | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | &mt RIGHT_SHIFT SLASH |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&mo 6` | LEFT_WIN<br>`&kp LEFT_WIN` | LEFT_ALT<br>`&kp LEFT_ALT` | lt2 SPACE<br>`&lt 2 SPACE` | lt2 SPACE<br>`&lt 2 SPACE` | mo1 (L center)<br>`&mo 1` | mo2<br>`&lt 1 ENTER` | lt1 ENTER<br>`&mo 2` | mo6 (R)<br>`&mo 6` | mo6 (R outer)<br>`&mo 6` |
| 単発タップ | &mo 6 | &kp LEFT_WIN | &kp LEFT_ALT | &lt 2 SPACE | &lt 2 SPACE | &mo 1 | &lt 1 ENTER | &mo 2 | &mo 6 | &mo 6 |
| ホールド | 〃 | 〃 | 〃 | &lt 2 SPACE | &lt 2 SPACE | 〃 | &lt 1 ENTER | 〃 | 〃 | 〃 |

### SYMBOL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&kp N1` | W<br>`&kp N2` | E<br>`&kp N3` | R<br>`&kp N4` | T<br>`&kp N5` | Y<br>`&kp N6` | U<br>`&kp N7` | I<br>`&kp N8` | O<br>`&kp N9` | P<br>`&kp N0` |
| 単発タップ | &kp N1 | &kp N2 | &kp N3 | &kp N4 | &kp N5 | &kp N6 | &kp N7 | &kp N8 | &kp N9 | &kp N0 |
| ■ Row 2 (home row) | A<br>`&mt LCTRL TAB` | S<br>`&kp GRAVE` | D<br>`&kp LEFT_BRACKET` | F<br>`&kp RIGHT_BRACKET` | G<br>`&kp DELETE` | H<br>`&kp BACKSPACE` | J<br>`&kp SEMICOLON` | K<br>`&kp SINGLE_QUOTE` | L<br>`&kp BACKSLASH` | -<br>`&trans` |
| 単発タップ | &mt LCTRL TAB | &kp GRAVE | &kp LEFT_BRACKET | &kp RIGHT_BRACKET | &kp DELETE | &kp BACKSPACE | &kp SEMICOLON | &kp SINGLE_QUOTE | &kp BACKSLASH | ▽ |
| ホールド | &mt LCTRL TAB | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| ■ Row 3 (Z row) | Z<br>`&mt LEFT_SHIFT ESCAPE` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&kp EQUAL` | ,<br>`&trans` | .<br>`&trans` | /<br>`&trans` |
| 単発タップ | &mt LEFT_SHIFT ESCAPE |  |  |  |  |  | &kp EQUAL | ▽ | ▽ | ▽ |
| ホールド | &mt LEFT_SHIFT ESCAPE |  |  |  |  |  | 〃 | 〃 | 〃 | 〃 |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&lt 3 SPACE` | lt2 SPACE<br>`&lt 3 SPACE` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&mo 3` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ | &lt 3 SPACE | &lt 3 SPACE |  |  | &mo 3 | ▽ |  |
| ホールド |  | 〃 | 〃 | &lt 3 SPACE | &lt 3 SPACE |  |  | 〃 | 〃 |  |

### VIM_NORMAL_1 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` |
| 単発タップ |  | mm_vim_w[0] → &kp LC(RIGHT) | &kp LC(RIGHT) | mm_vim_ctrl_r[0] → &none |  | mm_vim_shift_y[0] → td_vim_y[0] → &none | mm_vim_ctrl_u[0] → &kp LC(Z) |  | mm_vim_shift_o[0] → macro_vim_o | &kp LC(V) |
| ダブルタップ |  | 〃 | 〃 |  |  | mm_vim_shift_y[0] → td_vim_y[1] → macro_vim_yy | 〃 |  | 〃 | 〃 |
| Shift+ |  | 〃 | 〃 |  |  | mm_vim_shift_y[1] → macro_vim_shift_y | 〃 |  | mm_vim_shift_o[1] → macro_vim_shift_o | 〃 |
| Ctrl+ |  | mm_vim_w[1] → &kp LC(BACKSPACE) | 〃 | mm_vim_ctrl_r[1] → &kp LC(Y) |  |  | mm_vim_ctrl_u[1] → &kp PAGE_UP |  | 〃 | 〃 |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | -<br>`&kp RCTRL` |
| 単発タップ | &kp LCTRL |  | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[0] → &none |  | mm_vim_g[0] → td_vim_g[0] → &none | &kp LEFT | mm_vim_j[0] → &kp DOWN | &kp UP_ARROW | &kp RIGHT | &kp RCTRL |
| ダブルタップ | 〃 |  | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[1] → macro_vim_dd |  | mm_vim_g[0] → td_vim_g[1] → &kp LC(HOME) | 〃 | 〃 | 〃 | 〃 | 〃 |
| Shift+ | 〃 |  | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[1] → macro_vim_shift_d |  | mm_vim_g[1] → &kp LC(END) | 〃 | mm_vim_j[1] → macro_vim_join | 〃 | 〃 | 〃 |
| Ctrl+ | 〃 |  | mm_vim_ctrl_then_shift_d[1] → &kp PAGE_DOWN |  |  | 〃 | 〃 | 〃 | 〃 | 〃 |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | N<br>`&mm_vim_n` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | &kp LEFT_SHIFT | &kp DELETE |  | mm_vim_v[0] → &to 8 | &kp LC(LEFT) | mm_vim_n[0] → &kp F3 |  |  |  | &kp RIGHT_SHIFT |
| Shift+ | 〃 | 〃 |  | mm_vim_v[1] → macro_vim_v_line | 〃 | mm_vim_n[1] → &kp LS(F3) |  |  |  | 〃 |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&mo 3` | mo2<br>`&lt 3 ENTER` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  | &mo 3 | &lt 3 ENTER |  | ▽ |  |
| ホールド |  | 〃 | 〃 |  |  | 〃 | &lt 3 ENTER |  | 〃 |  |

### VIM_NORMAL_2 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` |
| 単発タップ |  |  |  | mm_vim_shift_4[0] → &none |  | mm_vim_shift_6[0] → &none |  |  |  | &kp HOME |
| Shift+ |  |  |  | mm_vim_shift_4[1] → &kp END |  | mm_vim_shift_6[1] → &kp HOME |  |  |  | 〃 |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&kp LEFT` | J<br>`&none` | K<br>`&none` | L<br>`&none` | -<br>`&kp RCTRL` |
| 単発タップ | &kp LCTRL |  |  |  |  | &kp LEFT |  |  |  | &kp RCTRL |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | &kp LEFT_SHIFT |  |  |  |  |  |  |  |  | &kp RIGHT_SHIFT |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  |  |  |  | ▽ |  |

### MOUSE レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 2 (home row) | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&mo 5` | L<br>`&none` | -<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  | &mo 5 |  |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### SCROLL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |
| ■ Row 2 (home row) | A<br>`&none` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&mkp MB1` | K<br>`&none` | L<br>`&mkp MB2` | -<br>`&none` |
| 単発タップ |  |  |  |  |  |  | &mkp MB1 |  | &mkp MB2 |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | N<br>`&none` | M<br>`&mkp MB4` | ,<br>`&none` | .<br>`&mkp MB5` | /<br>`&none` |
| 単発タップ |  |  |  |  |  |  | &mkp MB4 |  | &mkp MB5 |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### FUNCTION レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&kp F1` | W<br>`&kp F2` | E<br>`&kp F3` | R<br>`&kp F4` | T<br>`&kp F5` | Y<br>`&kp F6` | U<br>`&kp F7` | I<br>`&kp F8` | O<br>`&kp F9` | P<br>`&kp F10` |
| 単発タップ | &kp F1 | &kp F2 | &kp F3 | &kp F4 | &kp F5 | &kp F6 | &kp F7 | &kp F8 | &kp F9 | &kp F10 |
| ■ Row 2 (home row) | A<br>`&none` | S<br>`&sys_reset` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&sys_reset` | -<br>`&none` |
| 単発タップ |  | &sys_reset |  |  |  |  |  |  | &sys_reset |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&bootloader` | N<br>`&bootloader` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&none` |
| 単発タップ |  |  |  |  | &bootloader | &bootloader |  |  |  |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### BLUETOOTH レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&bt BT_SEL 0` | W<br>`&bt BT_SEL 1` | E<br>`&bt BT_SEL 2` | R<br>`&bt BT_SEL 3` | T<br>`&bt BT_SEL 4` | Y<br>`&none` | U<br>`&out OUT_USB` | I<br>`&none` | O<br>`&none` | P<br>`&none` |
| 単発タップ | &bt BT_SEL 0 | &bt BT_SEL 1 | &bt BT_SEL 2 | &bt BT_SEL 3 | &bt BT_SEL 4 |  | &out OUT_USB |  |  |  |
| ■ Row 2 (home row) | A<br>`&bt BT_CLR_ALL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&none` | J<br>`&none` | K<br>`&none` | L<br>`&none` | -<br>`&none` |
| 単発タップ | &bt BT_CLR_ALL |  |  |  |  |  |  |  |  |  |
| ■ Row 3 (Z row) | Z<br>`&none` | X<br>`&none` | C<br>`&bt BT_CLR` | V<br>`&none` | B<br>`&out OUT_BLE` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&none` |
| 単発タップ |  |  | &bt BT_CLR |  | &out OUT_BLE |  |  |  |  |  |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

### VIM_VISUAL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` |
| 単発タップ |  | &kp LS(LC(RIGHT)) | &kp LS(LC(RIGHT)) |  |  |  |  |  |  | macro_vim_visual_p |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | -<br>`&kp RCTRL` |
| 単発タップ | &kp LCTRL |  | macro_vim_visual_cut |  | mm_vim_visual_g[0] → td_vim_visual_g[0] → &none | &kp LS(LEFT) | &kp LS(DOWN) | &kp LS(UP) | &kp LS(RIGHT) | &kp RCTRL |
| ダブルタップ | 〃 |  | 〃 |  | mm_vim_visual_g[0] → td_vim_visual_g[1] → &kp LS(LC(HOME)) | 〃 | 〃 | 〃 | 〃 | 〃 |
| Shift+ | 〃 |  | 〃 |  | mm_vim_visual_g[1] → &kp LS(LC(END)) | 〃 | 〃 | 〃 | 〃 | 〃 |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&none` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | N<br>`&kp F3` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | &kp LEFT_SHIFT | macro_vim_visual_cut |  | macro_vim_visual_exit | &kp LS(LC(LEFT)) | &kp F3 |  |  |  | &kp RIGHT_SHIFT |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |

