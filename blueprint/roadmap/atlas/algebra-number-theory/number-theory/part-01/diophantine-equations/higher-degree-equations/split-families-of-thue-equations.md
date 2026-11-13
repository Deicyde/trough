---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSplitThueRecurrenceFamily, MetaMathlibExt.IsSplitThueRecurrenceFamily.three_le, MetaMathlibExt.isSplitThueRecurrenceFamily_example, MetaMathlibExt.splitThue_recurrence_solutions_bounded, MetaMathlibExt.splitThue_recurrence_solutions_eventually_trivial, MetaMathlibExt.splitThue_recurrence_roots_asymptotic, MetaMathlibExt.splitThue_recurrence_roots_growth, MetaMathlibExt.splitThue_recurrence_logUnitDet_asymptotic
statement: formalized
---

# Split families of Thue equations

8 results, 3 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html).

## Split Thue recurrence family

Let $d \in \mathbb{N}$, let $G_i(n)$ be integers for
$i, n \in \mathbb{N}$, and let $\gamma_i \in \mathbb{R}$ and $\delta_i \in \mathbb{C}$ for
$i \in \mathbb{N}$. Then $(d, G, \gamma, \delta)$ is a split Thue recurrence family when $d \ge 3$
and there are finite sets $R_i \subseteq \mathbb{C}$ and complex numbers $c_i(r)$
($i \in \mathbb{N}$, $r \in \mathbb{C}$) such that: for every $1 \le i \le d$, $c_i(r) \ne 0$
for all $r \in R_i$, $G_i(n) = \sum_{r \in R_i} c_i(r) r^n$ for all $n$, $\gamma_i \in R_i$,
and $|r| < \gamma_i$ for all $r \in R_i$ with $r \ne \gamma_i$; $\gamma_1 \ge 0$, $\gamma$ is
strictly increasing on $\{1, \dots, d - 1\}$, and $\gamma_{d-1} = \gamma_d$;
$c_{d-1}(\gamma_{d-1}) = c_d(\gamma_d)$; for $i \in \{d - 1, d\}$, $\delta_i \in R_i$,
$\delta_i \ne \gamma_i$, and $|r| < |\delta_i|$ for all $r \in R_i$ other than $\gamma_i$ and
$\delta_i$; and $|\delta_{d-1}| < |\delta_d| < \gamma_{d-2}$ and
$\gamma_{d-2}^2 < \gamma_d |\delta_d|$.

In words: each $G_i$ is a simple linear recurrence with dominant root $\gamma_i$, the sequences
$G_{d-1}$ and $G_d$ share their dominant root and its coefficient, and $\delta_{d-1}$, $\delta_d$
are their second dominant roots.

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Theorem 1 (conditions 1-3); dominant roots taken real and nonnegative as in the paper's standing assumption after Corollary 1.

Formalized by `MetaMathlibExt.IsSplitThueRecurrenceFamily`, a definition declared in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#is-split-thue-recurrence-family).

## A split Thue recurrence family has at least three sequences

If $(d, G, \gamma, \delta)$
is a split Thue recurrence family, then $d \ge 3$.

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Theorem 1 (the conditions mention `γ (d - 2)`).

Formalized by `MetaMathlibExt.IsSplitThueRecurrenceFamily.three_le`, a theorem declared in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#three-le).

## Example of a split Thue recurrence family

Let $G_1(n) = 3^n$, $G_2(n) = 5^n + 1$ and
$G_i(n) = 5^n + 2^n$ for $i \notin \{1, 2\}$; let $\gamma_1 = 3$ and $\gamma_i = 5$ for
$i \ne 1$; and let $\delta_2 = 1$ and $\delta_i = 2$ for $i \ne 2$. Then $(3, G, \gamma, \delta)$
is a split Thue recurrence family: the dominant roots of $G_1, G_2, G_3$ are $3, 5, 5$ and the
second dominant roots of $G_2, G_3$ are $1, 2$.

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Theorem 1 (conditions 1-3).

Formalized by `MetaMathlibExt.isSplitThueRecurrenceFamily_example`, a theorem declared in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#is-split-thue-recurrence-family-example).

## Hilgart's theorem on split families of Thue equations

Let $(d, G, \gamma, \delta)$ be a
split Thue recurrence family. Then there is $\kappa \in \mathbb{R}$ such that for every
$n \in \mathbb{N}$ and all integers $x, y$ with $|y| \ge 2$ and

$$(x - G_1(n) y) \cdots (x - G_d(n) y) - y^d = \pm 1$$

we have $\log |x| \le \kappa$, $\log |y| \le \kappa$ and $n \le \kappa$ (where $\log 0 = 0$).

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Theorem 1. The computability of `κ` is not recorded.

Stated but not proved: `MetaMathlibExt.splitThue_recurrence_solutions_bounded` is written with `theorem_wanted` in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#split-thue-recurrence-solutions-bounded).

## Split Thue families eventually have only trivial solutions

Let $(d, G, \gamma, \delta)$
be a split Thue recurrence family. Then there is $n_0$ such that for every $n \ge n_0$ and all
integers $x, y$,

$$(x - G_1(n) y) \cdots (x - G_d(n) y) - y^d = \pm 1$$

holds if and only if $(x, y) = (\pm 1, 0)$ or, for some $1 \le i \le d$,
$(x, y) = (G_i(n), 1)$ or $(x, y) = (-G_i(n), -1)$.

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Corollary 1. The computability of `n₀` is not recorded.

Stated but not proved: `MetaMathlibExt.splitThue_recurrence_solutions_eventually_trivial` is written with `theorem_wanted` in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#split-thue-recurrence-solutions-eventual).

## Asymptotics of the roots of a split Thue family

Let $(d, G, \gamma, \delta)$ be a split
Thue recurrence family. Call reals $\alpha_i(n)$ ($i, n \in \mathbb{N}$) an admissible labelling
if there is $N$ such that for all $n \ge N$ and $1 \le i \le d$,
$\prod_{k=1}^{d} (\alpha_i(n) - G_k(n)) = 1$ and $|\alpha_i(n) - G_i(n)| < 1$. Then, first,
there is $N$ such that for all $n \ge N$ every $z \in \mathbb{C}$ with
$\prod_{k=1}^{d} (z - G_k(n)) = 1$ is real; second, an admissible labelling exists; third, for
every admissible labelling $\alpha$ and every $1 \le i \le d$ there are $C \in \mathbb{R}$ and
$N$ such that for all $n \ge N$

$$|(\alpha_i(n) - G_i(n)) \prod_{k \ne i} (G_i(n) - G_k(n)) - 1| \le C \Gamma_i^{-n},$$

where the product is over $1 \le k \le d$ with $k \ne i$, and
$\Gamma_i = \gamma_i^{i-1} (\prod_{k=i+1}^{d-2} \gamma_k) \gamma_d^2$ if $i \le d - 2$ and
$\Gamma_i = \gamma_d^{d-2} |\delta_d|$ otherwise.

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Lemma 1. The `O`-term is written as `|(α⁽ⁱ⁾ - G i n) * ∏_{k ≠ i} (G i n - G k n) - 1| ≤ C * γ_ε⁻ⁿ`; `δ d` enters through its modulus.

Stated but not proved: `MetaMathlibExt.splitThue_recurrence_roots_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#split-thue-recurrence-roots-asymptotic).

## Growth of the roots of a split Thue family

Let $(d, G, \gamma, \delta)$ be a split Thue
recurrence family, and let $\alpha_i(n)$ ($i, n \in \mathbb{N}$) be reals for which there is $N$
such that for all $n \ge N$ and $1 \le i \le d$, $\prod_{k=1}^{d} (\alpha_i(n) - G_k(n)) = 1$
and $|\alpha_i(n) - G_i(n)| < 1$. Then there are $c > 0$ and $N'$ such that for all $n \ge N'$
and $1 \le i \le d$ we have $|\alpha_i(n)| \ge c \gamma_i^n$, and for every $1 \le j \le d$ with
$j \ne i$ both $|\alpha_i(n) - \alpha_j(n)|$ and $|\alpha_i(n) - G_j(n)|$ are at least
$c |\delta_d|^n$ if $\{i, j\} = \{d - 1, d\}$, and at least $c \max(\gamma_i, \gamma_j)^n$
otherwise.

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Lemma 2, including its last sentence (the same bounds with `α⁽ʲ⁾` replaced by `G j n`). `Ω` is the paper's lower bound `|f n| ≥ c * g n` for large `n`.

Stated but not proved: `MetaMathlibExt.splitThue_recurrence_roots_growth` is written with `theorem_wanted` in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#split-thue-recurrence-roots-growth).

## Determinants of logarithms in a split Thue family

Let $(d, G, \gamma, \delta)$ be a
split Thue recurrence family, let $\alpha_i(n)$ ($i, n \in \mathbb{N}$) be reals for which there
is $N$ such that for all $n \ge N$ and $1 \le i \le d$,
$\prod_{l=1}^{d} (\alpha_i(n) - G_l(n)) = 1$ and $|\alpha_i(n) - G_i(n)| < 1$, and let
$1 \le k \le d - 1$. Let $B_k(n)$ be the $k \times k$ matrix with entries
$\log |\alpha_i(n) - G_j(n)|$ for $1 \le i, j \le k$, where $\log 0 = 0$. Then there are
$c_1 > 0$, $c_2 > 0$ and $N'$ such that $c_1 n^k \le |\det B_k(n)| \le c_2 n^k$ for all
$n \ge N'$.

## Sources

- Tobias Hilgart, *On Split Families of Thue Equations with Linear Recurrence Sequences as Factors*, INTEGERS 25 (2025), Article A35, Lemma 3. `Real.log` is the logarithm of the absolute value; `Θ` is the paper's two-sided bound `c₁ n ^ k ≤ |det B_k| ≤ c₂ n ^ k` for large `n`.

Stated but not proved: `MetaMathlibExt.splitThue_recurrence_logUnitDet_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SplitThueRecurrenceWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html#split-thue-recurrence-log-unit-det-asymp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Split families of Thue equations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/split-families-of-thue-equations)
