---
declaration: section
origin: cited
lean: MetaMathlibExt.power_sum_rpow_one_div_le, MetaMathlibExt.power_sum_mul_div_max_le, MetaMathlibExt.power_sum_le_rpow_of_le, MetaMathlibExt.power_sum_le_card_mul_rpow_of_lt, MetaMathlibExt.sum_fib_rpow_le_of_two_le, MetaMathlibExt.sum_fib_rpow_le_card_mul_rpow, MetaMathlibExt.weighted_power_sum_mul_div_max_le, MetaMathlibExt.weighted_power_sum_le_mul_rpow_of_lt
statement: formalized
---

# Power sum inequalities for monotone sequences

11 results, 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html).

## Normalised power sums decrease in the exponent

Let $n \ge 0$ and let $x_1, \dots, x_n$
be positive real numbers. If $\alpha$ and $\beta$ are real numbers with $0 < \beta < \alpha$, then
$(\sum_{k=1}^{n} x_k^\alpha)^{1/\alpha} \le (\sum_{k=1}^{n} x_k^\beta)^{1/\beta}$.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Proposition 1.

Stated but not proved: `MetaMathlibExt.power_sum_rpow_one_div_le` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#power-sum-rpow-one-div-le).

## Lower bound for a power sum at the mean exponent

Let $0 < x_1 \le \dots \le x_N$ be
$N \ge 1$ real numbers, and for real $p$ write $S^{[p]} = \sum_{k=1}^{N} x_k^p$. For all real
$r, s > 0$,
$S^{[r]} S^{[s]} / \max(x_N^{r/2} S^{[s/2]}, x_N^{s/2} S^{[r/2]}) \le S^{[(r+s)/2]}$.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 2.

Stated but not proved: `MetaMathlibExt.power_sum_mul_div_max_le` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#power-sum-mul-div-max-le).

## Power sums under a larger exponent

Let $x_1, \dots, x_N$ be $N \ge 1$ positive real
numbers, and for real $p$ write $S^{[p]} = \sum_{k=1}^{N} x_k^p$. If $\alpha$ and $\beta$ are
real numbers with $0 < \beta \le \alpha$, then $S^{[\alpha]} \le (S^{[\beta]})^{\alpha/\beta}$.

In the paper $\alpha = (r + s)/2$ with $r, s > 0$ and the sequence is monotone; neither
assumption is needed here.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 2(i).

Stated but not proved: `MetaMathlibExt.power_sum_le_rpow_of_le` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#power-sum-le-rpow-of-le).

## Power mean bound for power sums with a smaller exponent

Let $x_1, \dots, x_N$ be
$N \ge 1$ positive real numbers, and for real $p$ write $S^{[p]} = \sum_{k=1}^{N} x_k^p$. If
$\alpha$ and $\beta$ are real numbers with $0 < \alpha < \beta$, then
$S^{[\alpha]} \le N (S^{[\beta]} / N)^{\alpha/\beta}$. If moreover $x_k \ge 1$ for every $k$,
then also $N (S^{[\beta]} / N)^{\alpha/\beta} \le S^{[\beta]}$.

In the paper $\alpha = (r + s)/2$ and the sequence is monotone, so the condition $x_k \ge 1$
for every $k$ is the paper's $x_1 \ge 1$.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 2(ii), including (4).

Stated but not proved: `MetaMathlibExt.power_sum_le_card_mul_rpow_of_lt` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#power-sum-le-card-mul-rpow-of-lt).

## Upper bound for Fibonacci power sums with exponent at least 2

Let $F_k$ denote the
$k$-th Fibonacci number. For every natural number $n \ge 1$ and every real $\alpha \ge 2$,
$\sum_{k=1}^{n} F_k^\alpha \le (F_n F_{n+1})^{\alpha/2}$.

In the paper $\alpha = (r + s)/2$.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 3(i).

Stated but not proved: `MetaMathlibExt.sum_fib_rpow_le_of_two_le` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#sum-fib-rpow-le-of-two-le).

## Upper bounds for Fibonacci power sums with exponent below 2

Let $F_k$ denote the $k$-th
Fibonacci number. For every natural number $n \ge 1$ and every real $\alpha$ with
$0 < \alpha < 2$,
$\sum_{k=1}^{n} F_k^\alpha \le n (F_n F_{n+1} / n)^{\alpha/2} \le F_n F_{n+1}$.

In the paper $\alpha = (r + s)/2$.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 3(ii).

Stated but not proved: `MetaMathlibExt.sum_fib_rpow_le_card_mul_rpow` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#sum-fib-rpow-le-card-mul-rpow).

## Lower bound for a weighted power sum at the mean exponent

Let
$0 < x_1 \le \dots \le x_N$ be $N \ge 1$ real numbers and $w_1, \dots, w_N$ positive real
weights, and for real $p$ write $S^{[p]} = \sum_{k=1}^{N} w_k x_k^p$. For all real $r, s > 0$,
$S^{[r]} S^{[s]} / \max(x_N^{r/2} S^{[s/2]}, x_N^{s/2} S^{[r/2]}) \le S^{[(r+s)/2]}$.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 4.

Stated but not proved: `MetaMathlibExt.weighted_power_sum_mul_div_max_le` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#weighted-power-sum-mul-div-max-le).

## Weighted power mean bound for power sums with a smaller exponent

Let
$x_1, \dots, x_N$ be $N \ge 1$ positive real numbers and $w_1, \dots, w_N$ positive real
weights, write $W = \sum_{k=1}^{N} w_k$, and for real $p$ write
$S^{[p]} = \sum_{k=1}^{N} w_k x_k^p$. If $\alpha$ and $\beta$ are real numbers with
$0 < \alpha < \beta$, then $S^{[\alpha]} \le W (S^{[\beta]} / W)^{\alpha/\beta}$. If moreover
$x_k \ge 1$ for every $k$, then also $W (S^{[\beta]} / W)^{\alpha/\beta} \le S^{[\beta]}$.

In the paper $\alpha = (r + s)/2$ and the sequence is monotone.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 4(ii).

Stated but not proved: `MetaMathlibExt.weighted_power_sum_le_mul_rpow_of_lt` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#weighted-power-sum-le-mul-rpow-of-lt).

## Weighted power-mean bounds for Fibonacci numbers

Let $F_k$ be the $k$-th Fibonacci
number ($F_1 = F_2 = 1$), let $n \ge 1$, let $w_1, \dots, w_n$ be positive reals with sum
$W = \sum_{k=1}^n w_k$, and let $\alpha$ be a real number with $0 < \alpha < 2$. Then

$$
\sum_{k=1}^n w_k F_k^{\alpha} \le
W \left( \frac{\sum_{k=1}^n w_k F_k^2}{W} \right)^{\alpha/2} \le \sum_{k=1}^n w_k F_k^2.
$$

In the source the exponent is $\alpha = (r + s)/2$.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 5(ii).

Stated but not proved: `MetaMathlibExt.weighted_sum_fib_rpow_le_mul_rpow` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#weighted-sum-fib-rpow-le-mul-rpow).

## Classical Fibonacci sum identities

Let $F_k$ denote the $k$-th Fibonacci number, with
$F_0 = 0$ and $F_1 = 1$. For every natural number $n \ge 1$, the following identities hold in
the integers: $\sum_{i=1}^{n} F_{2i-1} = F_{2n}$; $\sum_{i=1}^{n} F_{2i} = F_{2n+1} - 1$;
$\sum_{i=1}^{n} i F_i = n F_{n+2} - F_{n+3} + 2$;
$\sum_{i=1}^{n} F_i F_{3i} = F_n F_{n+1} F_{2n+1}$; and
$\sum_{i=1}^{n} \binom{n}{i} F_i = F_{2n}$.

These are parts (b), (c), (d), (e) and (g) of Lemma 1 of the paper, quoted there from Koshy.

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Lemma 1.

Stated but not proved: `MetaMathlibExt.fib_power_sum_identities` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#fib-power-sum-identities).

## Product of two Fibonacci power sums

Let $F_k$ denote the $k$-th Fibonacci number. For
every natural number $n \ge 1$ and all real $r, s$ with $r + s \ge 4$,
$(F_n F_{n+1})^2 \le (\sum_{k=1}^{n} F_k^r)(\sum_{k=1}^{n} F_k^s)$, where $F_k^r$ and $F_k^s$ are
real powers, with equality if and only if $n = 1$, or $n = 2$, or $n \ge 3$ and $r = s = 2$.

The paper quotes this result from its reference [2].

## Sources

- Sanja Kovač and Josip Pečarić, *Power Sum Inequalities for Monotone Sequences with Applications to Fibonacci Numbers*, INTEGERS 26 (2026), Article A101, Theorem 1.

Stated but not proved: `MetaMathlibExt.sum_fib_rpow_mul_sum_fib_rpow_ge` is written with `theorem_wanted` in [WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MonotonePowerSumInequalitiesWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html#sum-fib-rpow-mul-sum-fib-rpow-ge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Power sum inequalities for monotone sequences](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/inequalities/power-sum-inequalities-for-monotone-sequences)
