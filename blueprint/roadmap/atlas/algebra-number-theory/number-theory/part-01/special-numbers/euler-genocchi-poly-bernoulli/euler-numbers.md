---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven_zero, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven_step, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven_recurrence, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.ramanujan_part1_ch5_entry10b_euleriansymmetry
statement: formalized
proof: formalized
---

# Euler numbers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers/index.html).

## Even-index Euler numbers

The integers $E_0, E_2, E_4, \dots$ defined recursively by
$E_0 = 1$ and $E_{2m} = -\sum_{k=0}^{m-1} \binom{2m}{2k} E_{2k}$ for $m \ge 1$; equivalently,
$\sum_{k=0}^{m} \binom{2m}{2k} E_{2k}$ is $1$ for $m = 0$ and $0$ for $m \ge 1$. The value at
$n$ is $E_{2n}$.

The first values are $E_0 = 1$, $E_2 = -1$, $E_4 = 5$, $E_6 = -61$; the absolute values are the
secant numbers.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers/index.html#chapter5-euler-even).

## The initial even-index Euler number

$E_0 = 1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven_zero`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers/index.html#chapter5-euler-even-zero).

## Recursion for the even-index Euler numbers

For every natural number $m \ge 1$,
$E_{2m} = -\sum_{k=0}^{m-1} \binom{2m}{2k} E_{2k}$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven_step`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers/index.html#chapter5-euler-even-step).

## Binomial recurrence for the even-index Euler numbers

For every natural number $m$,
$\sum_{k=0}^{m} \binom{2m}{2k} E_{2k}$ is $1$ if $m = 0$ and $0$ if $m \ge 1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.chapter5EulerEven_recurrence`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers/index.html#chapter5-euler-even-recurrence).

## Bernoulli numbers as a convolution of even-index Euler numbers

For every natural number
$n$, $2^{2n} (2^{2n} - 1) B_{2n} = 2n \sum_{k=0}^{n-1} \binom{2n-2}{2k} E_{2k} E_{2n-2k-2}$, where
$B_m$ are the Bernoulli numbers and $E_{2k}$ are the even-index Euler numbers.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry10bEuleriansymmetry.ramanujan_part1_ch5_entry10b_euleriansymmetry`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry10bEuleriansymmetry.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers/index.html#ramanujan-part1-ch5-entry10b-euleriansym).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/euler-numbers)
