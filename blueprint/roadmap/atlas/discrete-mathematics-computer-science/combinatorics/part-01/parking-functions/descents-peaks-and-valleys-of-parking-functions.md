---
declaration: section
origin: cited
lean: MetaMathlibExt.total_descents_over_parking_functions, MetaMathlibExt.parkingFunction_descent_genFun, MetaMathlibExt.parkingFunction_descentSet_card_eq_ascentSet_reflect, MetaMathlibExt.parkingFunction_descentSet_card_eq_ascentSet, MetaMathlibExt.parkingFunction_descentSet_card_reflect, MetaMathlibExt.sum_ndpf_multisetDescent_eq, MetaMathlibExt.parkingFunction_descentSet_recursion, MetaMathlibExt.parkingFunction_descentSet_initial_card
statement: formalized
---

# Descents, peaks and valleys of parking functions

34 results, 7 proved and 27 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html).

## Total number of descents over parking functions

Let $n$ be a natural number. A descent of
a function $f \colon \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ is an index $i$ with $i + 1 < n$
and $f(i) > f(i+1)$. Summed over all parking functions
$f \colon \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ of length $n$, the number of descents is
$\binom{n}{2} (n+1)^{n-2}$, which is $0$ for $n < 2$.

Parking functions are taken in threshold form: for each $k < n$, at most $n - k$ of the values
$f(i)$ are at least $k$. This is equivalent to the source's sorted-preference formulation.

## Sources

- Paul R. F. Schumacher, "Descents in Parking Functions," Journal of Integer Sequences 21 (2018), Article 18.2.3, Theorem, line 180, https://cs.uwaterloo.ca/journals/JIS/VOL21/Schumacher/schu5.tex

Formalized by `MetaMathlibExt.total_descents_over_parking_functions`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TotalDescentsParkingFunctions.lean, line 881](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/TotalDescentsParkingFunctions.lean#L881). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#total-descents-over-parking-functions).

## Descent generating function of parking functions

Write a sequence of length $n$ as
$(a_1, \dots, a_n)$; its descents are the $j \in \{1, \dots, n-1\}$ with $a_j > a_{j+1}$, and
$\operatorname{des}$ is their number. A parking function $f$ of length $n$ is read as the sequence
$a_j = f(j-1) + 1$. Let $PF_n$ be the set of parking functions of length $n$, $PF^{\uparrow}_n$
the set of nondecreasing ones, and $d(n, j)$ the number of $\alpha \in PF_n$ with
$\operatorname{des}(\alpha) = j$. For every $n \ge 1$, in the polynomial ring $\mathbb{N}[y]$,

$$\sum_{\alpha \in PF_n} y^{\operatorname{des}(\alpha)} = \sum_{j=0}^{n-1} d(n, j)\, y^j =
\sum_{\beta \in PF^{\uparrow}_n} \sum_{\pi} y^{\operatorname{des}(\pi)},$$

where, for each $\beta$, $\pi$ runs over the rearrangements of $\beta$: the sequences of length
$n$ with the same multiset of entries as $\beta$.

The paper prints the middle sum from $j = 1$; it is read from $j = 0$ (at $n = 1$ the printed
middle sum is $0$ while the other two sides are $1$). At $n = 0$ the left side is $1$ and the
middle sum is empty, so $n \ge 1$ is assumed, as in the paper.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorems 1 and 2 (`jis-2024-24.8.6-thm-1`, `jis-2024-24.8.6-thm-2`).

Stated but not proved: `MetaMathlibExt.parkingFunction_descent_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#parking-function-descent-gen-fun).

## Descent sets versus reflected ascent sets of parking functions

Write a parking function
$f$ of length $n$ as the sequence $(a_1, \dots, a_n)$ with $a_j = f(j-1) + 1$. Its descent set is
the set of $j \in \{1, \dots, n-1\}$ with $a_j > a_{j+1}$, and its ascent set the set of such $j$
with $a_j < a_{j+1}$. For every $n$ and every $I \subseteq \{1, \dots, n-1\}$, let
$J = \{n - i : i \in I\}$. Then the number of parking functions of length $n$ with descent set
$I$ equals the number of parking functions of length $n$ with ascent set $J$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Proposition 6 (`jis-2024-24.8.6-prop-6`).

Stated but not proved: `MetaMathlibExt.parkingFunction_descentSet_card_eq_ascentSet_reflect` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#parking-function-descent-set-card-eq-asc).

## Descent sets and ascent sets of parking functions are equidistributed

Write a parking
function $f$ of length $n$ as the sequence $(a_1, \dots, a_n)$ with $a_j = f(j-1) + 1$. Its
descent set is the set of $j \in \{1, \dots, n-1\}$ with $a_j > a_{j+1}$, and its ascent set the
set of such $j$ with $a_j < a_{j+1}$. For every $n$ and every $I \subseteq \{1, \dots, n-1\}$, the
number of parking functions of length $n$ with descent set $I$ equals the number of parking
functions of length $n$ with ascent set $I$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Corollary 15 (`jis-2024-24.8.6-cor-15`).

Stated but not proved: `MetaMathlibExt.parkingFunction_descentSet_card_eq_ascentSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#parking-function-descent-set-card-eq-asc-2).

## Reflection symmetry of descent sets of parking functions

Write a parking function $f$ of
length $n$ as the sequence $(a_1, \dots, a_n)$ with $a_j = f(j-1) + 1$. Its descent set is the set
of $j \in \{1, \dots, n-1\}$ with $a_j > a_{j+1}$. For every $n$ and every
$I \subseteq \{1, \dots, n-1\}$, let $J = \{n - i : i \in I\}$. Then the number of parking
functions of length $n$ with descent set $I$ equals the number with descent set $J$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorem 16 (`jis-2024-24.8.6-thm-16`).

Stated but not proved: `MetaMathlibExt.parkingFunction_descentSet_card_reflect` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#parking-function-descent-set-card-reflec).

## Counting parking functions with a given descent set by their content

The descent set
of a word $w = (w_1, \dots, w_n)$ is $\{i : 1 \le i \le n - 1,\ w_i > w_{i+1}\}$. Let
$n \in \mathbb{N}$ and $I \subseteq \{1, \dots, n - 1\}$. Then the number of parking functions of
length $n$ with descent set $I$ equals the sum, over the nondecreasing parking functions $\beta$
of length $n$, of the number of words of length $n$ with descent set $I$ whose multiset of
letters is the multiset of entries of $\beta$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 17 (`jis-2024-24.8.6-lem-17`).

Stated but not proved: `MetaMathlibExt.sum_ndpf_multisetDescent_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#sum-ndpf-multiset-descent-eq).

## Recursion for parking functions with a given descent set

The descent set of a word
$w = (w_1, \dots, w_\ell)$ is $\{i : 1 \le i \le \ell - 1,\ w_i > w_{i+1}\}$, and $d(J; n)$ denotes
the number of parking functions of length $n$ with descent set $J$. Let $n \in \mathbb{N}$, let
$I \subseteq \{1, \dots, n - 1\}$ be nonempty with largest element $m$, and let
$I^- = I \setminus \{m\}$. Then

$$d(I; n) = \sum_{\beta} \sum_{X} d_X(I^-) - d(I^-; n),$$

where $\beta$ runs over the nondecreasing parking functions of length $n$, $X$ runs over the
distinct sub-multisets of size $m$ of the multiset of entries of $\beta$, and $d_X(I^-)$ is the
number of words of length $m$ whose multiset of letters is $X$ and whose descent set is $I^-$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorem 18 (`jis-2024-24.8.6-thm-18`).

Stated but not proved: `MetaMathlibExt.parkingFunction_descentSet_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#parking-function-descent-set-recursion).

## Parking functions with descent set $\{1, \dots, k\}$

Let $n \ge 1$ and
$0 \le k \le n - 1$. The number of parking functions $(a_1, \dots, a_n)$ of length $n$ whose descent
set $\{i : 1 \le i \le n - 1,\ a_i > a_{i+1}\}$ is exactly $\{1, \dots, k\}$ (empty when $k = 0$)
equals $\frac{1}{n}\binom{n}{k}\binom{2n-k}{n-k-1}$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Proposition 24 (`jis-2024-24.8.6-prop-24`).

Stated but not proved: `MetaMathlibExt.parkingFunction_descentSet_initial_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#parking-function-descent-set-initial-car).

## Peakless-tieless parking functions are counted by the Catalan numbers

Write a parking
function $f$ of length $n$ as the sequence $(a_1, \dots, a_n)$ with $a_j = f(j-1) + 1$. It is
peakless-tieless if there is no $j$ with $a_{j-1} < a_j > a_{j+1}$ (a peak) and no $j$ with
$a_j = a_{j+1}$ (a tie). For every $n \ge 1$, the number of peakless-tieless parking functions of
length $n$ is the Catalan number $C_n$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Corollary 31 (`jis-2024-24.8.6-cor-31`).

Stated but not proved: `MetaMathlibExt.card_peakless_tieless_parkingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#card-peakless-tieless-parking-function).

## Peakless-tieless parking functions by last entry

Write a parking function $f$ of length
$n$ as the sequence $(a_1, \dots, a_n)$ with $a_j = f(j-1) + 1 \in \{1, \dots, n\}$. It is
peakless-tieless if there is no $j$ with $a_{j-1} < a_j > a_{j+1}$ (a peak) and no $j$ with
$a_j = a_{j+1}$ (a tie). For natural numbers $i$ and $n$ with $1 \le i \le n$, the number of
peakless-tieless parking functions of length $n$ with last entry $a_n = i$ is

$$\binom{n+i-2}{i-1} \cdot \frac{n-i+1}{n}.$$

This is the Catalan-triangle entry $T(n-1, i-1)$ of OEIS A009766.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Corollary 32 (`jis-2024-24.8.6-cor-32`).

Stated but not proved: `MetaMathlibExt.card_peakless_tieless_parkingFunction_last` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#card-peakless-tieless-parking-function-l).

## Valleyless-tieless parking functions are counted by the Fine numbers

Write a parking
function $f$ of length $n$ as the sequence $(a_1, \dots, a_n)$ with $a_j = f(j-1) + 1$. It is
valleyless-tieless if there is no $j$ with $a_{j-1} > a_j < a_{j+1}$ (a valley) and no $j$ with
$a_j = a_{j+1}$ (a tie). For every $n \ge 1$, the number of valleyless-tieless parking functions
of length $n$ is the Fine number $F(n+1)$, where the Fine numbers are indexed from $0$ with
$F(0) = 1$; for $n = 1, \dots, 5$ these counts are $1, 2, 6, 18, 57$.

In the offset-0 indexing of OEIS A000957 ($0, 1, 0, 1, 2, 6, 18, \dots$), $F(n+1)$ is the term
of index $n + 2$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorem 33 (`jis-2024-24.8.6-thm-33`).

Stated but not proved: `MetaMathlibExt.card_valleyless_tieless_parkingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#card-valleyless-tieless-parking-function).

## Prepending $1$ to valleyless-tieless parking functions

Identify a parking function $f$
of length $m$ with the word $(f(0) + 1, \dots, f(m-1) + 1)$. A word $(a_1, \dots, a_m)$ has a
tie if $a_k = a_{k+1}$ for some $k$, and a valley if $a_{k-1} > a_k < a_{k+1}$ for some $k$;
write $\mathrm{VTPF}_m$ for the set of parking functions of length $m$ with no ties and no
valleys. For $n \ge 1$, the map $(a_1, \dots, a_n) \mapsto (1, a_1 + 1, \dots, a_n + 1)$ is a
bijection from $\mathrm{VTPF}_n$ onto the set of $(b_1, \dots, b_{n+1}) \in \mathrm{VTPF}_{n+1}$
with $b_1 = 1$ and $b_{n+1} > 1$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 34 (`jis-2024-24.8.6-lem-34`).

Stated but not proved: `MetaMathlibExt.valleyless_tieless_prepend_one_bijOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#valleyless-tieless-prepend-one-bij-on).

## First and last entries of peakless-tieless parking functions

A parking function
$(a_1, \dots, a_m)$ is peakless-tieless if $a_i \ne a_{i+1}$ for all $1 \le i \le m - 1$ and there
is no $i$ with $a_{i-1} < a_i > a_{i+1}$. Let $G_m$, $E_m$ and $L_m$ be the sets of
peakless-tieless parking functions of length $m$ with $a_1 > a_m$, $a_1 = a_m$ and $a_1 < a_m$,
respectively. Then $|E_{n+1}| = |L_n|$ for every $n \ge 1$, and $|G_{n+1}| = |L_{n+1}|$ for every
$n \ge 0$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 40 (`jis-2024-24.8.6-lem-40`).

Stated but not proved: `MetaMathlibExt.peakless_tieless_ends_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#peakless-tieless-ends-card).

## Peakless-tieless parking functions with first entry below the last

For every
$n \in \mathbb{N}$, the number of parking functions $(a_1, \dots, a_{n+1})$ of length $n + 1$
with no ties (no $i$ with $a_i = a_{i+1}$), no peaks (no $i$ with $a_{i-1} < a_i$ and
$a_i > a_{i+1}$) and $a_1 < a_{n+1}$ is the Fine number $F(n + 1)$, indexed from $0$ so that
$F(0) = 1$.

In the indexing of OEIS A000957, $F(n + 1)$ is the term of index $n + 2$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorem 41 (`jis-2024-24.8.6-thm-41`).

Stated but not proved: `MetaMathlibExt.card_peakless_tieless_first_lt_last` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#card-peakless-tieless-first-lt-last).

## Peakless parking functions with $n - 1$ ties

For every $n \ge 1$, exactly one parking
function $(a_1, \dots, a_n)$ of length $n$ has no peaks (no $i$ with $a_{i-1} < a_i$ and
$a_i > a_{i+1}$) and exactly $n - 1$ ties (indices $i \in \{1, \dots, n - 1\}$ with
$a_i = a_{i+1}$).

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 42 (`jis-2024-24.8.6-lem-42`).

Stated but not proved: `MetaMathlibExt.card_peakless_parkingFunction_max_ties` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#card-peakless-parking-function-max-ties).

## Every statistic encoding comes from a parking function

Write a parking function $f$ of
length $n$ as the sequence $(a_1, \dots, a_n)$ with $a_j = f(j-1) + 1$. Its statistic encoding is
the word $w_1 \cdots w_{n-1}$ over the letters $A$, $D$, $T$ with $w_j = A$ if $a_j < a_{j+1}$
(an ascent), $w_j = D$ if $a_j > a_{j+1}$ (a descent) and $w_j = T$ if $a_j = a_{j+1}$ (a tie).
For every natural number $n$, every word of length $n - 1$ over $A$, $D$, $T$ (the empty word
when $n = 0$) is the statistic encoding of some parking function of length $n$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorem 48 (`jis-2024-24.8.6-thm-48`).

Stated but not proved: `MetaMathlibExt.exists_parkingFunction_statEnc` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#exists-parking-function-stat-enc).

## Uniquely encoded parking functions have steps of at most one and no gaps

The statistic
encoding of $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ is the word over $\{A, D, T\}$ whose
letter at each position $0 \le i \le n - 2$ is $A$, $D$ or $T$ according as $f(i) < f(i+1)$,
$f(i) > f(i+1)$ or $f(i) = f(i+1)$. Let $f$ be a parking function of length $n$ such that every
parking function of length $n$ with the same statistic encoding equals $f$. Then
$|f(i+1) - f(i)| \le 1$ for all $0 \le i \le n - 2$, and for all $q < p$ in $\{0, \dots, n-1\}$,
if $p$ is a value of $f$ then so is $q$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 49 (`jis-2024-24.8.6-lem-49`).

Stated but not proved: `MetaMathlibExt.unique_statEnc_adjacent_and_downward_closed` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#unique-stat-enc-adjacent-and-downward-cl).

## The sorted rearrangement of a uniquely encoded parking function

The statistic encoding
of $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ is the word over $\{A, D, T\}$ whose letter at
each position $0 \le i \le n - 2$ is $A$, $D$ or $T$ according as $f(i) < f(i+1)$,
$f(i) > f(i+1)$ or $f(i) = f(i+1)$. Let $f$ be a parking function of length $n$ such that every
parking function of length $n$ with the same statistic encoding equals $f$, and let
$\beta : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ be nondecreasing and take each value as often
as $f$ does. Then the statistic encoding of $\beta$ consists of $A$'s followed by $T$'s (either
block may be empty).

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 50 (`jis-2024-24.8.6-lem-50`).

Stated but not proved: `MetaMathlibExt.unique_statEnc_sorted_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#unique-stat-enc-sorted-form).

## Valley plateaus of a uniquely encoded parking function equal $1$

For a map
$g : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$, its statistic encoding is the word of length
$n - 1$ whose $k$-th letter, for $1 \le k \le n - 1$, is $<$, $=$ or $>$ according as
$g(k-1) < g(k)$, $g(k-1) = g(k)$ or $g(k-1) > g(k)$. Let $f$ be a parking function of length $n$
such that every parking function of length $n$ with the same statistic encoding as $f$ equals
$f$, and write $\alpha_k = f(k-1) + 1$ for $1 \le k \le n$. If $2 \le i \le j \le n - 1$,
$\alpha_{i-1} > \alpha_i$, $\alpha_k = \alpha_i$ for every $k$ with $i \le k \le j$, and
$\alpha_j < \alpha_{j+1}$, then $\alpha_k = 1$ for every $k$ with $i \le k \le j$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 51 (`jis-2024-24.8.6-lem-51`).

Stated but not proved: `MetaMathlibExt.unique_statEnc_valley_plateau_eq_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#unique-stat-enc-valley-plateau-eq-one).

## Statistic encodings with a unique parking function

The statistic encoding of a parking
function $(a_1, \dots, a_n)$ is the word $w_1 \cdots w_{n-1}$ over $\{A, D, T\}$ with $w_i = A$ if
$a_i < a_{i+1}$, $w_i = D$ if $a_i > a_{i+1}$ and $w_i = T$ if $a_i = a_{i+1}$. For every
$n \in \mathbb{N}$, a word over $\{A, D, T\}$ with one letter for each $1 \le i \le n - 1$ is the
statistic encoding of exactly one parking function of length $n$ if and only if it consists of
$A$'s followed by $T$'s or of $T$'s followed by $D$'s (either block may be empty).

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorem 52 (`jis-2024-24.8.6-thm-52`).

Stated but not proved: `MetaMathlibExt.unique_parkingFunction_statEnc_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#unique-parking-function-stat-enc-iff).

## Tie-and-value map

Let $n \in \mathbb{N}$ and $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$.
The ties of $f$ are the positions $i \in \{1, \dots, n-1\}$ with $f(i-1) = f(i)$, and its values
are the elements of the image of $f$. Form the list of the ties in decreasing order followed by
the values in increasing order. Then $\varphi_n(f) : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ is the
map whose value at $k$ is the entry of this list at position $k$ (counting from $0$), or $k$
itself if the list has at most $k$ entries.

For nondecreasing $f$ the list has exactly $n$ entries. In the paper's one-based notation,
$\varphi$ sends $\alpha = (a_1, \dots, a_n)$ to its tie set $\{j + 1 : a_j = a_{j+1}\}$ in
decreasing order followed by its value set in increasing order.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, the function `φ` of Theorem 30 (`jis-2024-24.8.6-thm-30`), defined as in arXiv:2312.16786v1, Definition 4.2.

Formalized by `MetaMathlibExt.peaklessTielessOfNondecreasing`, a definition declared in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#peakless-tieless-of-nondecreasing).

## Example of the tie-and-value map

For $n = 6$, the tie-and-value map $\varphi$ sends
$(0, 0, 1, 2, 3, 3)$ to $(5, 1, 0, 1, 2, 3)$; in the paper's one-based values this reads
$\varphi(1, 1, 2, 3, 4, 4) = (6, 2, 1, 2, 3, 4)$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, the function `φ` of Theorem 30, Example (arXiv:2312.16786v1, Example 4.3).

Formalized by `MetaMathlibExt.peaklessTielessOfNondecreasing_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#peakless-tieless-of-nondecreasing-exampl).

## Nondecreasing and peakless-tieless parking functions are in bijection

For every
$n \in \mathbb{N}$, the tie-and-value map $\varphi$ is a bijection from the nondecreasing parking
functions of length $n$ onto the peakless-tieless parking functions of length $n$, that is, the
parking functions $(a_1, \dots, a_n)$ with $a_i \ne a_{i+1}$ for all $1 \le i \le n - 1$ and no $i$
with $a_{i-1} < a_i > a_{i+1}$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Theorem 30 (`jis-2024-24.8.6-thm-30`; arXiv:2312.16786v1, Theorem 4.4).

Stated but not proved: `MetaMathlibExt.peaklessTielessOfNondecreasing_bijOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#peakless-tieless-of-nondecreasing-bij-on).

## Fuel-bounded ascent-to-descent rearrangement

For a fuel $N \in \mathbb{N}$ and a word
$x = x_1 \cdots x_m$ over $\mathbb{N}$, the word $\nu_N(x)$ is defined by recursion on $N$:
$\nu_0(x) = x$, and $\nu_{N+1}(x) = x$ when $m \le 1$. For $m \ge 2$, let $A$ be the set of
positions of the least letter of $x$ and $B$ the set of positions of its greatest letter. If
$b \le a$ for all $a \in A$ and $b \in B$ (Case 1), put $i = \max A$ and $j = \min B$; then
$\nu_{N+1}(x) = \nu_N(x_1 \cdots x_{j-1})\, x_i\, \nu_N(x_{j+1} \cdots x_{i-1})\, x_j\,
\nu_N(x_{i+1} \cdots x_m)$. Otherwise (Case 2), let $i$ be the greatest $a \in A$ such that
$a < b$ for some $b \in B$, and $j$ the least $b \in B$ with $b > i$; then
$\nu_{N+1}(x) = \nu_N(x_1 \cdots x_{i-1})\, x_j\, \nu_N(x_{i+1} \cdots x_{j-1})\, x_i\,
\nu_N(x_{j+1} \cdots x_m)$.

Every recursive call is on a strictly shorter word, so fuel $N = m$ never runs out.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Definition `nu` (Section 2).

Formalized by `MetaMathlibExt.ascentToDescentRearrangementAux`, a definition declared in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#ascent-to-descent-rearrangement-aux).

## Ascent-to-descent rearrangement

For a word $x = x_1 \cdots x_m$ over $\mathbb{N}$, the
ascent-to-descent rearrangement of $x$ is $\nu(x) = \nu_m(x)$, the fuel-bounded
ascent-to-descent rearrangement $\nu_N(x)$ with fuel $N = m$, the length of $x$.

Every recursive call of $\nu_N$ is on a strictly shorter word, so the fuel $m$ never runs out.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Definition `nu` (Section 2).

Formalized by `MetaMathlibExt.ascentToDescentRearrangement`, a definition declared in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#ascent-to-descent-rearrangement).

## Words of length at most one are fixed by the ascent-to-descent rearrangement

Every word
$x$ over $\mathbb{N}$ of length at most $1$ satisfies $\nu(x) = x$, where $\nu$ is the
ascent-to-descent rearrangement.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Definition `nu`, Case 0.

Formalized by `MetaMathlibExt.ascentToDescentRearrangement_of_length_le_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#ascent-to-descent-rearrangement-of-lengt).

## Example of the ascent-to-descent rearrangement

The ascent-to-descent rearrangement $\nu$
satisfies $\nu(1\,4\,1\,3\,4\,3\,1\,2\,1) = 4\,1\,4\,3\,1\,1\,2\,1\,3$, $\nu(1\,4) = 4\,1$ and
$\nu(3\,1\,2\,1) = 1\,2\,1\,3$.

The last two are the sub-steps of the first: $\nu(1\,4)$ falls under Case 2 of the definition
and $\nu(3\,1\,2\,1)$ under Case 1.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Example following Definition `nu`.

Formalized by `MetaMathlibExt.ascentToDescentRearrangement_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#ascent-to-descent-rearrangement-example).

## Ascents of a word are the descents of its rearrangement

For a word
$x = x_1 \cdots x_m$ over $\mathbb{N}$, let the ascent set $\mathrm{Asc}(x)$ be the set of
$i \in \{1, \dots, m - 1\}$ with $x_i < x_{i+1}$, and the descent set $\mathrm{Des}(x)$ the set
of $i \in \{1, \dots, m - 1\}$ with $x_i > x_{i+1}$. Then every word $x$ over $\mathbb{N}$
satisfies $\mathrm{Asc}(x) = \mathrm{Des}(\nu(x))$, where $\nu$ is the ascent-to-descent
rearrangement.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 11 (`jis-2024-24.8.6-lem-11`).

Stated but not proved: `MetaMathlibExt.ascList_eq_desList_ascentToDescentRearrangement` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#asc-list-eq-des-list-ascent-to-descent-r).

## The ascent-to-descent rearrangement is injective

The ascent-to-descent rearrangement
$\nu$ is injective on finite words over $\mathbb{N}$: if $\nu(x) = \nu(x')$, then $x = x'$.

Since $\nu$ rearranges letters, this is the same as injectivity of $\nu$ on the rearrangements of
each fixed word.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 13 (`jis-2024-24.8.6-lem-13`).

Stated but not proved: `MetaMathlibExt.ascentToDescentRearrangement_injective` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#ascent-to-descent-rearrangement-injectiv).

## The ascent-to-descent rearrangement matches ascent and descent sets

Let $y$ be a finite
word over $\mathbb{N}$ and $I$ a finite set of natural numbers. For a word $x = x_1 \cdots x_m$,
let the ascent set $\mathrm{Asc}(x)$ be the set of $i \in \{1, \dots, m - 1\}$ with
$x_i < x_{i+1}$, and the descent set $\mathrm{Des}(x)$ the set of those $i$ with $x_i > x_{i+1}$.
Then the ascent-to-descent rearrangement $\nu$ maps the set of rearrangements $x$ of $y$ with
$\mathrm{Asc}(x) = I$ bijectively onto the set of rearrangements $x$ of $y$ with
$\mathrm{Des}(x) = I$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Proposition 10 (`jis-2024-24.8.6-prop-10`).

Stated but not proved: `MetaMathlibExt.ascentToDescentRearrangement_bijOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#ascent-to-descent-rearrangement-bij-on).

## Flicking valleyless-tieless parking functions

Identify a parking function $f$ of length
$m$ with the word $(f(0) + 1, \dots, f(m-1) + 1)$. A word $(a_1, \dots, a_m)$ has a tie if
$a_k = a_{k+1}$ for some $k$, a peak if $a_{k-1} < a_k > a_{k+1}$ for some $k$, and a valley if
$a_{k-1} > a_k < a_{k+1}$ for some $k$. For $1 \le i \le m$, let
$\mathrm{flick}_i(x_1, \dots, x_m) = (x_i, x_{i-1}, \dots, x_1, x_m, x_{m-1}, \dots, x_{i+1})$,
the block $x_m, \dots, x_{i+1}$ being empty when $i = m$. Let $D$ be the set of parking
functions $(a_1, \dots, a_{n+1})$ with no valleys and no ties such that $a_1 = 1$ and
$a_{n+1} > 1$, and let $\varphi$ send $v \in D$ to $\mathrm{flick}_i(v)$, where $i$ is the
position of the strictly largest entry of $v$. Then $\varphi$ is a bijection from $D$ onto the
set of parking functions $(b_1, \dots, b_{n+1})$ with no peaks and no ties such that
$b_1 > b_{n+1}$.

The paper's domain condition $a_{i+1} > 1$ is a typo for $a_{n+1} > 1$, its domain in the same
display.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Proposition 37 (`jis-2024-24.8.6-prop-37`).

Stated but not proved: `MetaMathlibExt.valleyless_tieless_flick_bijOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#valleyless-tieless-flick-bij-on).

## Gudmundsson's bijection between Dyck words and standard Young tableaux

For every $n$
there is a map $f$ from Dyck words to semistandard Young tableaux of the two-row shape $(n, n)$
with the following two properties. First, for every Dyck word $w$ of semilength $n$ and every
$i \ge 1$, if the $i$th letter of $w$ is an up step $U$ then $i$ is an entry of the first row of
$f(w)$, and if it is a down step $D$ then $i$ is an entry of the second row. Second, $f$
restricts to a bijection from the Dyck words of semilength $n$ onto the standard tableaux of
shape $(n, n)$, that is, those whose $2n$ entries are distinct and lie in $\{1, \dots, 2n\}$.

Since $f(w)$ is standard, $i$ lies in the first row of $f(w)$ exactly when the $i$th letter of $w$
is $U$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 22 (Gudmundsson, Theorem 6) (`jis-2024-24.8.6-lem-22`).

Stated but not proved: `MetaMathlibExt.exists_dyckWord_standardYoungTableau_bijOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#exists-dyck-word-standard-young-tableau).

## Dyck words and nondecreasing parking functions

For every $n$ there is a map $g$ from Dyck
words to maps $\{0, \dots, n-1\} \to \{0, \dots, n-1\}$ such that, for every Dyck word $w$ of
semilength $n$ and every $i < n$, $g(w)(i)$ is the number of down steps $D$ of $w$ before its
$(i+1)$st up step $U$, and $g$ restricts to a bijection from the Dyck words of semilength $n$
onto the nondecreasing parking functions of length $n$.

With one-based entries, the $i$th entry of the parking function is one plus the number of $D$s
before the $i$th $U$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 23 (`jis-2024-24.8.6-lem-23`).

Stated but not proved: `MetaMathlibExt.exists_dyckWord_nondecreasing_parkingFunction_bijOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#exists-dyck-word-nondecreasing-parking-f).

## Peakless parking functions with $n - 2$ ties

For every $n \ge 2$, the number of parking
functions $(a_1, \dots, a_n)$ of length $n$ that have no peaks (no $i$ with $a_{i-1} < a_i$ and
$a_i > a_{i+1}$) and exactly $n - 2$ ties (indices $i \in \{1, \dots, n - 1\}$ with
$a_i = a_{i+1}$) is $(n - 1)n$.

The paper prints $n(n + 1)$, which contradicts its own table ($2, 6, 12, 20, 30$ for
$n = 2, \dots, 6$); its proof counts tuples with $i$ leading ones followed by $n - i \ge 1$
copies of one value, so $1 \le i \le n - 1$ and each monotone direction contributes
$\sum_{i=1}^{n-1} i$.

## Sources

- Ari Cruz, Pamela E. Harris, Kimberly J. Harry, Jan Kretschmann, Matt McClinton, Alex Moon, John O. Museus and Eric Redmon, *On Some Discrete Statistics of Parking Functions*, Journal of Integer Sequences 27 (2024), Article 24.8.6, Lemma 43 (`jis-2024-24.8.6-lem-43`).

Stated but not proved: `MetaMathlibExt.card_peakless_parkingFunction_ties_eq_sub_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ParkingFunctionStatisticsWanted.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html#card-peakless-parking-function-ties-eq-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Descents, peaks and valleys of parking functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/parking-functions/descents-peaks-and-valleys-of-parking-functions)
