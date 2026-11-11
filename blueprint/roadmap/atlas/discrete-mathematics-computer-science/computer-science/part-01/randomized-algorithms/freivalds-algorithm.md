---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Matrix.freivaldsTrial, Cslib.Algorithms.Lean.Matrix.freivaldsTrial_time, Cslib.Algorithms.Lean.Matrix.freivaldsMatrix, Cslib.Algorithms.Lean.Matrix.freivaldsTrial_accept_iff, Cslib.Algorithms.Lean.Matrix.freivaldsTrial_accept_discrepancy_iff, Cslib.Algorithms.Lean.Matrix.freivaldsTrial_complete, Cslib.Algorithms.Lean.Matrix.freivaldsTrial_empty, Cslib.Algorithms.Lean.Matrix.freivaldsTrial_acceptanceCard_bound
statement: formalized
proof: formalized
---

# Freivalds' algorithm

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html).

## Freivalds trial

Given $n \times n$ matrices $A$, $B$, $C$ over
$\mathbb{F}_2 = \mathbb{Z}/2$, stored as arrays of rows, and a seed $r \in \mathbb{F}_2^n$, the
trial computes the column vectors $Br$, $A(Br)$ and $Cr$, each by accumulating matrix products
into a zero column, and returns true exactly when $A(Br) = Cr$. Its cost is the pair (number of
scalar multiplications, number of scalar additions), each multiply-add step counting one of each.

The coefficient domain is $\mathbb{F}_2$ by intentional specialization, not by a restriction in
the cited source.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial).

## Cost of the Freivalds trial

For $n \times n$ matrices $A$, $B$, $C$ over
$\mathbb{F}_2$ and every seed $r \in \mathbb{F}_2^n$, the Freivalds trial performs exactly
$3n^2$ scalar multiplications and exactly $3n^2$ scalar additions.

These counts belong to the same run that returns the acceptance bit and include the additions
into the zero-initialized accumulators.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-time).

## Matrix of a Freivalds input

An $n \times n$ array $A$ of rows over
$\mathbb{F}_2 = \mathbb{Z}/2$ determines the $n \times n$ matrix over $\mathbb{F}_2$ whose
$(i, j)$ entry is entry $j$ of row $i$ of $A$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsMatrix`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-matrix).

## Acceptance criterion of the Freivalds trial

For $n \times n$ matrices $A$, $B$, $C$ over
$\mathbb{F}_2$ and every seed $r \in \mathbb{F}_2^n$, the Freivalds trial on $A$, $B$, $C$, $r$
returns true if and only if $A(Br) = Cr$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_accept_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-accept-iff).

## Acceptance via the product discrepancy

For $n \times n$ matrices $A$, $B$, $C$ over
$\mathbb{F}_2$ and every seed $r \in \mathbb{F}_2^n$, the Freivalds trial on $A$, $B$, $C$, $r$
returns true if and only if $(AB - C)r = 0$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_accept_discrepancy_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-accept-discrepancy-iff).

## Completeness of the Freivalds trial

Let $A$, $B$, $C$ be $n \times n$ matrices over
$\mathbb{F}_2$ with $AB = C$. Then for every seed $r \in \mathbb{F}_2^n$ the Freivalds trial on
$A$, $B$, $C$, $r$ returns true. This includes the case $n = 0$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-complete).

## Freivalds trial on empty matrices

For $0 \times 0$ matrices $A$, $B$, $C$ over
$\mathbb{F}_2$ and the empty seed $r$, the Freivalds trial returns true at zero cost: it performs
no scalar multiplications and no scalar additions.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Basic.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-empty).

## Soundness of the Freivalds trial

Let $A$, $B$, $C$ be $n \times n$ matrices over
$\mathbb{F}_2$ with $AB \ne C$. Then twice the number of seeds $r \in \mathbb{F}_2^n$ on which the
Freivalds trial returns true is at most the number of all seeds in $\mathbb{F}_2^n$; that is, at
most half of the seeds accept.

Acceptance is the return value of the same charged run whose cost is counted.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_acceptanceCard_bound`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Counting.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Counting.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-acceptance-card-bound).

## Freivalds trial law

For $n \times n$ matrices $A$, $B$, $C$ over
$\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$, given as arrays, the Freivalds trial law is the
probability distribution on $\{\mathrm{true}, \mathrm{false}\}$ of the value returned by the
Freivalds trial on $A$, $B$, $C$ with seed $r$, where $r$ is drawn uniformly from
$\mathbb{F}_2^n$.

The seeds are exactly uniform; no pseudorandom generator or assumed error probability is
involved.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrialLaw`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-law).

## Uniform mass of a Freivalds seed

Let $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$. For every
$n$ and every vector $r \in \mathbb{F}_2^n$, the uniform probability distribution on
$\mathbb{F}_2^n$ assigns to $r$ the probability $(2^n)^{-1}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsSeed_pointMass`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-seed-point-mass).

## Acceptance probability of the Freivalds trial as a seed count

Let $A$, $B$, $C$ be
$n \times n$ matrices over $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$, given as arrays. The
probability that the Freivalds trial law of $A$, $B$, $C$ returns true equals the number of
seeds $r \in \mathbb{F}_2^n$ on which the Freivalds trial on $A$, $B$, $C$ with seed $r$
accepts, divided by the number $|\mathbb{F}_2^n|$ of all seeds.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrialLaw_acceptance`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-law-acceptance).

## The Freivalds trial accepts a correct product with probability one

Let $A$, $B$, $C$ be
$n \times n$ matrices over $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$, given as arrays. If
$AB = C$, then the Freivalds trial law of $A$, $B$, $C$ returns true with probability $1$.
This includes the case $n = 0$ of empty matrices.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrialLaw_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-law-complete).

## The Freivalds trial accepts a wrong product with probability at most one half

Let $A$,
$B$, $C$ be $n \times n$ matrices over $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$, given as arrays.
If $AB \ne C$, then the Freivalds trial law of $A$, $B$, $C$ returns true with probability at
most $1/2$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrialLaw_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Probability.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-law-sound).

## Repeated Freivalds test on fixed seeds

Given $n \times n$ matrices $A$, $B$, $C$ over
$\mathbb{Z}/2$ and seeds $r_0, \dots, r_{k-1} \in (\mathbb{Z}/2)^n$, run the Freivalds trial on
$A$, $B$, $C$ with each seed $r_0, \dots, r_{k-1}$ in order, including the trials after a
rejection, and return the conjunction of their results (true when $k = 0$). The arithmetic cost
of the run is the sum of the costs of the $k$ trials.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeat`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat).

## Cost of the repeated Freivalds test on fixed seeds

For $n \times n$ matrices $A$, $B$,
$C$ over $\mathbb{Z}/2$ and seeds $r_0, \dots, r_{k-1} \in (\mathbb{Z}/2)^n$, the repeated
Freivalds test on these seeds performs exactly $3kn^2$ scalar multiplications and $3kn^2$ scalar
additions.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeat_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-time).

## Acceptance of the repeated Freivalds test on fixed seeds

For $n \times n$ matrices
$A$, $B$, $C$ over $\mathbb{Z}/2$ and seeds $r_0, \dots, r_{k-1} \in (\mathbb{Z}/2)^n$, the
repeated Freivalds test on these seeds accepts if and only if, for every $i < k$, the Freivalds
trial on $A$, $B$, $C$ with seed $r_i$ accepts.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeat_accept_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-accept-iff).

## Completeness of the repeated Freivalds test on fixed seeds

Let $A$, $B$, $C$ be
$n \times n$ matrices over $\mathbb{Z}/2$ with $AB = C$. Then for every $k$, including $k = 0$,
and all seeds $r_0, \dots, r_{k-1} \in (\mathbb{Z}/2)^n$, the repeated Freivalds test on these
seeds accepts.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeat_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-complete).

## Repeated Freivalds test with no trials

For $n \times n$ matrices $A$, $B$, $C$ over
$\mathbb{Z}/2$, the repeated Freivalds test on the empty list of seeds ($k = 0$) accepts and
performs no scalar multiplications or additions.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeat_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-zero).

## Repeated Freivalds test on empty matrices

For $0 \times 0$ matrices $A$, $B$, $C$ over
$\mathbb{Z}/2$ and any number $k$ of seeds (each the empty vector), the repeated Freivalds test
accepts and performs no scalar multiplications or additions.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeat_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Repeat.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-empty).

## Output distribution of repeated Freivalds trials

For natural numbers $n, k$ and
$n \times n$ matrices $A, B, C$ over $\mathbb{F}_2$, this is the probability distribution on
$\{\mathrm{true}, \mathrm{false}\}$ of the result returned by the repeated Freivalds executor on
$A, B, C$ when its history of $k$ seeds is drawn uniformly from $(\mathbb{F}_2^n)^k$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeatLaw`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-law).

## Uniform mass of a Freivalds seed history

For all natural numbers $n$ and $k$, under the
uniform distribution on histories of $k$ seeds, that is, on $(\mathbb{F}_2^n)^k$, every history
has probability exactly $(2^{nk})^{-1}$. This includes the cases $k = 0$ and $n = 0$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsHistory_pointMass`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-history-point-mass).

## Counting accepted histories of repeated Freivalds trials

Let $n, k$ be natural numbers
and let $A, B, C$ be $n \times n$ matrices over $\mathbb{F}_2$. The number of histories
$(r_1, \dots, r_k)$ of seeds $r_i \in \mathbb{F}_2^n$ on which the repeated Freivalds executor
accepts equals $a^k$, where $a$ is the number of seeds $r \in \mathbb{F}_2^n$ on which a single
Freivalds trial accepts.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeat_acceptanceCard`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-acceptance-card).

## Acceptance probability of repeated Freivalds trials

Let $n, k$ be natural numbers and
let $A, B, C$ be $n \times n$ matrices over $\mathbb{F}_2$. If the history of $k$ seeds is drawn
uniformly from $(\mathbb{F}_2^n)^k$, the probability that the repeated Freivalds executor accepts
is $p^k$, where $p$ is the probability that a single Freivalds trial accepts on a seed drawn
uniformly from $\mathbb{F}_2^n$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeatLaw_acceptance_power`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-law-acceptance-power).

## Completeness of repeated Freivalds trials

Let $n, k$ be natural numbers and let
$A, B, C$ be $n \times n$ matrices over $\mathbb{F}_2$ with $AB = C$. If the history of $k$
seeds is drawn uniformly from $(\mathbb{F}_2^n)^k$, then the repeated Freivalds executor accepts
with probability $1$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeatLaw_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-law-complete).

## Soundness of repeated Freivalds trials

Let $n, k$ be natural numbers and let
$A, B, C$ be $n \times n$ matrices over $\mathbb{F}_2$ with $AB \ne C$. If the history of $k$
seeds is drawn uniformly from $(\mathbb{F}_2^n)^k$, then the repeated Freivalds executor accepts
with probability at most $(2^k)^{-1}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeatLaw_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Amplification.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-law-sound).

## The sharp Freivalds example has a wrong product

Let $A = B = (1)$ and $C = (0)$ be
$1 \times 1$ matrices over $\mathbb{Z}/2\mathbb{Z}$. Then $AB \neq C$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivalds_one_wrong`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-one-wrong).

## The sharp Freivalds example accepts exactly the zero seed

Let $A = B = (1)$ and
$C = (0)$ be $1 \times 1$ matrices over $\mathbb{Z}/2\mathbb{Z}$. For every seed
$r \in (\mathbb{Z}/2\mathbb{Z})^1$, the Freivalds trial on $A$, $B$, $C$ with seed $r$, which
compares $A(Br)$ with $Cr$, accepts if and only if the single entry $r_0$ of $r$ is $0$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_one_accept_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-one-accept-iff).

## The sharp Freivalds example has exactly one accepted seed

Let $A = B = (1)$ and
$C = (0)$ be $1 \times 1$ matrices over $\mathbb{Z}/2\mathbb{Z}$. Exactly one seed
$r \in (\mathbb{Z}/2\mathbb{Z})^1$ is accepted by the Freivalds trial on $A$, $B$, $C$.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrial_one_acceptanceCard`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-one-acceptance-card).

## The sharp Freivalds example is accepted with probability one half

Let $A = B = (1)$
and $C = (0)$ be $1 \times 1$ matrices over $\mathbb{Z}/2\mathbb{Z}$. When the seed is drawn
uniformly from $(\mathbb{Z}/2\mathbb{Z})^1$, the Freivalds trial on $A$, $B$, $C$ accepts with
probability exactly $1/2$.

Since $AB \neq C$, this shows that the bound $1/2$ on the probability that one trial accepts a
wrong product cannot be improved.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsTrialLaw_one_sharp`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-trial-law-one-sharp).

## Exact acceptance probability of repeated trials on the sharp Freivalds example

Let
$A = B = (1)$ and $C = (0)$ be $1 \times 1$ matrices over $\mathbb{Z}/2\mathbb{Z}$, and let $k$
be a natural number. Run $k$ Freivalds trials on $A$, $B$, $C$ with seeds drawn independently and
uniformly from $(\mathbb{Z}/2\mathbb{Z})^1$, accepting exactly when every trial accepts. Then the
run accepts with probability exactly $2^{-k}$.

Since $AB \neq C$, the bound $2^{-k}$ on the probability that $k$ trials accept a wrong product
cannot be improved.

Formalized by `Cslib.Algorithms.Lean.Matrix.freivaldsRepeatLaw_one_sharp`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Freivalds/Sharpness.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html#freivalds-repeat-law-one-sharp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Freivalds' algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/randomized-algorithms/freivalds-algorithm)
