---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.expectedTime, Cslib.Algorithms.Lean.TimeM.uniformPermutation, Cslib.Algorithms.Lean.TimeM.uniformPermutation_length, Cslib.Algorithms.Lean.TimeM.uniformPermutation_perm, Cslib.Algorithms.Lean.TimeM.expectedTime_uniformPermutation, Cslib.Algorithms.Lean.TimeM.expectedTime_eq_of_time_eq, Cslib.Algorithms.Lean.TimeM.expectedTime_uniformPermutation_eq_of_time_eq, Cslib.Algorithms.Lean.TimeM.expectedTime_uniformPermutation_toReal
statement: formalized
proof: formalized
---

# Average-case running time

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html).

## Expected running time

Let $A$ be an algorithm on inputs of a type $\gamma$ whose running
time $T_A(x)$ on each input $x$ is a natural number, and let $D$ be a probability mass function on
$\gamma$. The expected running time of $A$ under $D$ is the extended nonnegative expectation
$\sum_{x \in \gamma} D(x)\, T_A(x) \in [0, \infty]$ of the running time, the sum taken over all
inputs.

Valuing the expectation in $[0, \infty]$ records a divergent expected time as $\infty$; a
real-valued integral would collapse it to $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.expectedTime`, a definition declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#expected-time).

## Uniformly random rearrangement of a list

For a list $x = (x_0, \dots, x_{n-1})$, the
uniform permutation of $x$ is the probability distribution on lists obtained by choosing a
permutation $\sigma$ of $\{0, \dots, n-1\}$ uniformly at random and outputting
$(x_{\sigma(0)}, \dots, x_{\sigma(n-1)})$.

Formalized by `Cslib.Algorithms.Lean.TimeM.uniformPermutation`, a definition declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#uniform-permutation).

## Rearrangements preserve length

For a list $x$, every list in the support of the uniform
permutation of $x$ has the same length as $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.uniformPermutation_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#uniform-permutation-length).

## Rearrangements are permutations

For a list $x$, every list in the support of the uniform
permutation of $x$ is a permutation of $x$, that is, it has the same entries with the same
multiplicities.

Formalized by `Cslib.Algorithms.Lean.TimeM.uniformPermutation_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#uniform-permutation-perm).

## Average formula for the expected time over random orderings

Let $A$ be an algorithm on
lists whose running time $T_A(y)$ on each list $y$ is a natural number, and let
$x = (x_0, \dots, x_{n-1})$ be a list of length $n$. The expected running time of $A$ when its
input is $x$ rearranged by a uniformly random permutation equals

$$\frac{1}{n!} \sum_{\sigma} T_A(x_{\sigma(0)}, \dots, x_{\sigma(n-1)}),$$

the sum running over all permutations $\sigma$ of $\{0, \dots, n-1\}$ and computed in
$[0, \infty]$.

Formalized by `Cslib.Algorithms.Lean.TimeM.expectedTime_uniformPermutation`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#expected-time-uniform-permutation).

## Constant running time on the support gives that expected time

Let $A$ be an algorithm
on inputs of a type $\gamma$ whose running time $T_A(x)$ on each input $x$ is a natural number,
let $D$ be a probability mass function on $\gamma$, and let $c$ be a natural number. If
$T_A(x) = c$ for every input $x$ in the support of $D$, then the expected running time of $A$
under $D$ equals $c$.

Inputs outside the support have probability $0$, so their running times do not contribute.

Formalized by `Cslib.Algorithms.Lean.TimeM.expectedTime_eq_of_time_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#expected-time-eq-of-time-eq).

## Constant running time on all rearrangements gives that expected time

Let $A$ be an
algorithm on lists whose running time $T_A(y)$ on each list $y$ is a natural number, let
$x = (x_0, \dots, x_{n-1})$ be a list of length $n$, and let $c$ be a natural number. If
$T_A(x_{\sigma(0)}, \dots, x_{\sigma(n-1)}) = c$ for every permutation $\sigma$ of
$\{0, \dots, n-1\}$, then the expected running time of $A$ when its input is $x$ rearranged by a
uniformly random permutation equals $c$.

Formalized by `Cslib.Algorithms.Lean.TimeM.expectedTime_uniformPermutation_eq_of_time_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#expected-time-uniform-permutation-eq-of).

## Average formula for the expected time over random orderings, in the reals

Let $A$ be an
algorithm on lists whose running time $T_A(y)$ on each list $y$ is a natural number, and let
$x = (x_0, \dots, x_{n-1})$ be a list of length $n$. The expected running time of $A$ when its
input is $x$ rearranged by a uniformly random permutation, converted from $[0, \infty]$ to a real
number, equals

$$\frac{1}{n!} \sum_{\sigma} T_A(x_{\sigma(0)}, \dots, x_{\sigma(n-1)}),$$

the sum running over all permutations $\sigma$ of $\{0, \dots, n-1\}$ and computed in $\mathbb{R}$.

Every term of the average is a natural number, so the expected time is finite and the conversion
loses nothing.

Formalized by `Cslib.Algorithms.Lean.TimeM.expectedTime_uniformPermutation_toReal`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/ExpectedCost.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html#expected-time-uniform-permutation-to-rea).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Average-case running time](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/average-case-running-time/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/randomized-algorithms/average-case-running-time)
