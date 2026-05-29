# キー割り当て一覧

※ 3 個のレイヤーのキー割り当てを 1 ファイルに集約。各レイヤー 42 バインディング位置を「動作」セクションでまとめてから「経路」セクションに進む。

- 各 row セクション行に「キーラベル」と「バインディング (`&...`)」の 2 段表示でキー位置を示す。
- 各表の左端 1 列が「操作」（単発タップ / ホールド / ダブルタップ / Shift+ / Ctrl+）または「■ Row N」見出し。

## 動作

### VIM_NORMAL_1 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` |  |
| 単発タップ |  | Ctrl+→ | Ctrl+→ |  |  |  | Ctrl+Z |  | END ▸ ENTER | Ctrl+V |  |
| ダブルタップ |  | 〃 | 〃 |  |  | HOME ▸ Shift+END ▸ Ctrl+C | 〃 |  | 〃 | 〃 |  |
| Shift+ |  | 〃 | 〃 |  |  | Shift+END ▸ Ctrl+C | 〃 |  | HOME ▸ ENTER ▸ ↑ | 〃 |  |
| Ctrl+ |  | Ctrl+BS | 〃 | Ctrl+Y |  |  | PgUp |  | 〃 | 〃 |  |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | -<br>`&kp RCTRL` |  |
| 単発タップ | LCtrl |  |  |  |  | ← | ↓ | ↑ | → | RCtrl |  |
| ダブルタップ | 〃 |  | HOME ▸ Shift+END ▸ Ctrl+X |  | Ctrl+HOME | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| Shift+ | 〃 |  | Shift+END ▸ Ctrl+X |  | Ctrl+END | 〃 | END ▸ DEL ▸ SPACE | 〃 | 〃 | 〃 |  |
| Ctrl+ | 〃 |  | PgDn |  |  | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center mo7)<br>`&none` | N<br>`&mm_vim_n` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | LShift | DEL |  | ⇒L8 | Ctrl+← |  | F3 |  |  |  | RShift |
| Shift+ | 〃 | 〃 |  | HOME ▸ Shift+↓ ▸ レイヤー 8 へ | 〃 |  | Shift+F3 |  |  |  | 〃 |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&mo 3` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  | L3 |  |  | ENTER | ▽ |  |
| ホールド |  | 〃 | 〃 |  |  | 〃 |  |  | L3 | 〃 |  |

### VIM_NORMAL_2 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` |  |
| 単発タップ |  |  |  |  |  |  |  |  |  | HOME |  |
| Shift+ |  |  |  | END |  | HOME |  |  |  | 〃 |  |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&kp LEFT` | J<br>`&none` | K<br>`&none` | L<br>`&none` | -<br>`&kp RCTRL` |  |
| 単発タップ | LCtrl |  |  |  |  | ← |  |  |  | RCtrl |  |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | LShift |  |  |  |  |  |  |  |  |  | RShift |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  |  |  |  |  | ▽ |  |

### VIM_VISUAL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` |  |
| 単発タップ |  | Shift+Ctrl+→ | Shift+Ctrl+→ |  |  |  |  |  |  | LShift ▸ RShift ▸ Ctrl+V ▸ レイヤー 0 へ |  |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | -<br>`&kp RCTRL` |  |
| 単発タップ | LCtrl |  | LShift ▸ RShift ▸ Ctrl+X ▸ レイヤー 0 へ |  |  | Shift+← | Shift+↓ | Shift+↑ | Shift+→ | RCtrl |  |
| ダブルタップ | 〃 |  | 〃 |  | Shift+Ctrl+HOME | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| Shift+ | 〃 |  | 〃 |  | Shift+Ctrl+END | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&none` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center mo7)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | LShift | LShift ▸ RShift ▸ Ctrl+X ▸ レイヤー 0 へ |  | LShift ▸ RShift ▸ → ▸ レイヤー 0 へ | Shift+Ctrl+← |  | F3 |  |  |  | RShift |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |

## 経路

### VIM_NORMAL_1 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&mm_vim_w` | E<br>`&kp LC(RIGHT)` | R<br>`&mm_vim_ctrl_r` | T<br>`&none` | Y<br>`&mm_vim_shift_y` | U<br>`&mm_vim_ctrl_u` | I<br>`&none` | O<br>`&mm_vim_shift_o` | P<br>`&kp LC(V)` |  |
| 単発タップ |  | mm_vim_w[0] → &kp LC(RIGHT) | &kp LC(RIGHT) | mm_vim_ctrl_r[0] → &none |  | mm_vim_shift_y[0] → td_vim_y[0] → &none | mm_vim_ctrl_u[0] → &kp LC(Z) |  | mm_vim_shift_o[0] → macro_vim_o | &kp LC(V) |  |
| ダブルタップ |  | 〃 | 〃 |  |  | mm_vim_shift_y[0] → td_vim_y[1] → macro_vim_yy | 〃 |  | 〃 | 〃 |  |
| Shift+ |  | 〃 | 〃 |  |  | mm_vim_shift_y[1] → macro_vim_shift_y | 〃 |  | mm_vim_shift_o[1] → macro_vim_shift_o | 〃 |  |
| Ctrl+ |  | mm_vim_w[1] → &kp LC(BACKSPACE) | 〃 | mm_vim_ctrl_r[1] → &kp LC(Y) |  |  | mm_vim_ctrl_u[1] → &kp PAGE_UP |  | 〃 | 〃 |  |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&mm_vim_ctrl_then_shift_d` | F<br>`&none` | G<br>`&mm_vim_g` | H<br>`&kp LEFT` | J<br>`&mm_vim_j` | K<br>`&kp UP_ARROW` | L<br>`&kp RIGHT` | -<br>`&kp RCTRL` |  |
| 単発タップ | &kp LCTRL |  | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[0] → &none |  | mm_vim_g[0] → td_vim_g[0] → &none | &kp LEFT | mm_vim_j[0] → &kp DOWN | &kp UP_ARROW | &kp RIGHT | &kp RCTRL |  |
| ダブルタップ | 〃 |  | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[0] → td_vim_d[1] → macro_vim_dd |  | mm_vim_g[0] → td_vim_g[1] → &kp LC(HOME) | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| Shift+ | 〃 |  | mm_vim_ctrl_then_shift_d[0] → mm_vim_shift_d[1] → macro_vim_shift_d |  | mm_vim_g[1] → &kp LC(END) | 〃 | mm_vim_j[1] → macro_vim_join | 〃 | 〃 | 〃 |  |
| Ctrl+ | 〃 |  | mm_vim_ctrl_then_shift_d[1] → &kp PAGE_DOWN |  |  | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&kp DELETE` | C<br>`&none` | V<br>`&mm_vim_v` | B<br>`&kp LC(LEFT)` | (center mo7)<br>`&none` | N<br>`&mm_vim_n` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | &kp LEFT_SHIFT | &kp DELETE |  | mm_vim_v[0] → &to 8 | &kp LC(LEFT) |  | mm_vim_n[0] → &kp F3 |  |  |  | &kp RIGHT_SHIFT |
| Shift+ | 〃 | 〃 |  | mm_vim_v[1] → macro_vim_v_line | 〃 |  | mm_vim_n[1] → &kp LS(F3) |  |  |  | 〃 |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&mo 3` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&lt 3 ENTER` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  | &mo 3 |  |  | &lt 3 ENTER | ▽ |  |
| ホールド |  | 〃 | 〃 |  |  | 〃 |  |  | &lt 3 ENTER | 〃 |  |

### VIM_NORMAL_2 レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&none` | E<br>`&none` | R<br>`&mm_vim_shift_4` | T<br>`&none` | Y<br>`&mm_vim_shift_6` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&kp HOME` |  |
| 単発タップ |  |  |  | mm_vim_shift_4[0] → &none |  | mm_vim_shift_6[0] → &none |  |  |  | &kp HOME |  |
| Shift+ |  |  |  | mm_vim_shift_4[1] → &kp END |  | mm_vim_shift_6[1] → &kp HOME |  |  |  | 〃 |  |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&none` | F<br>`&none` | G<br>`&none` | H<br>`&kp LEFT` | J<br>`&none` | K<br>`&none` | L<br>`&none` | -<br>`&kp RCTRL` |  |
| 単発タップ | &kp LCTRL |  |  |  |  | &kp LEFT |  |  |  | &kp RCTRL |  |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&none` | C<br>`&none` | V<br>`&none` | B<br>`&none` | (center mo7)<br>`&none` | N<br>`&none` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | &kp LEFT_SHIFT |  |  |  |  |  |  |  |  |  | &kp RIGHT_SHIFT |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&trans` | LEFT_ALT<br>`&trans` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&trans` | mo6 (R outer)<br>`&none` |
| 単発タップ |  | ▽ | ▽ |  |  |  |  |  |  | ▽ |  |

### VIM_VISUAL レイヤー

| 操作 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ■ Row 1 (QWERTY 上段) | Q<br>`&none` | W<br>`&kp LS(LC(RIGHT))` | E<br>`&kp LS(LC(RIGHT))` | R<br>`&none` | T<br>`&none` | Y<br>`&none` | U<br>`&none` | I<br>`&none` | O<br>`&none` | P<br>`&macro_vim_visual_p` |  |
| 単発タップ |  | &kp LS(LC(RIGHT)) | &kp LS(LC(RIGHT)) |  |  |  |  |  |  | macro_vim_visual_p |  |
| ■ Row 2 (home row) | A<br>`&kp LCTRL` | S<br>`&none` | D<br>`&macro_vim_visual_cut` | F<br>`&none` | G<br>`&mm_vim_visual_g` | H<br>`&kp LS(LEFT)` | J<br>`&kp LS(DOWN)` | K<br>`&kp LS(UP)` | L<br>`&kp LS(RIGHT)` | -<br>`&kp RCTRL` |  |
| 単発タップ | &kp LCTRL |  | macro_vim_visual_cut |  | mm_vim_visual_g[0] → td_vim_visual_g[0] → &none | &kp LS(LEFT) | &kp LS(DOWN) | &kp LS(UP) | &kp LS(RIGHT) | &kp RCTRL |  |
| ダブルタップ | 〃 |  | 〃 |  | mm_vim_visual_g[0] → td_vim_visual_g[1] → &kp LS(LC(HOME)) | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| Shift+ | 〃 |  | 〃 |  | mm_vim_visual_g[1] → &kp LS(LC(END)) | 〃 | 〃 | 〃 | 〃 | 〃 |  |
| ■ Row 3 (Z row) | Z<br>`&kp LEFT_SHIFT` | X<br>`&macro_vim_visual_cut` | C<br>`&none` | V<br>`&macro_vim_visual_exit` | B<br>`&kp LS(LC(LEFT))` | (center mo7)<br>`&none` | N<br>`&kp F3` | M<br>`&none` | ,<br>`&none` | .<br>`&none` | /<br>`&kp RIGHT_SHIFT` |
| 単発タップ | &kp LEFT_SHIFT | macro_vim_visual_cut |  | macro_vim_visual_exit | &kp LS(LC(LEFT)) |  | &kp F3 |  |  |  | &kp RIGHT_SHIFT |
| ■ Row 4 (thumb) | mo6 (L outer)<br>`&none` | LEFT_WIN<br>`&none` | LEFT_ALT<br>`&none` | lt2 SPACE<br>`&none` | lt2 SPACE<br>`&none` | mo1 (L center)<br>`&none` | mo2<br>`&none` | mo7 (raised)<br>`&none` | lt1 ENTER<br>`&none` | mo6 (R)<br>`&none` | mo6 (R outer)<br>`&none` |
| 単発タップ |  |  |  |  |  |  |  |  |  |  |  |

