---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.hireAssistant, Cslib.Algorithms.Lean.TimeM.hireAssistant_ret, Cslib.Algorithms.Lean.TimeM.hireAssistant_hires, Cslib.Algorithms.Lean.TimeM.hireAssistant_time, Cslib.Algorithms.Lean.TimeM.hireAssistant_nil, Cslib.Algorithms.Lean.TimeM.hireAssistant_singleton, Cslib.Algorithms.Lean.TimeM.hireAssistant_hire_bounds, Cslib.Algorithms.Lean.TimeM.hireAssistant_increasing
statement: formalized
proof: formalized
---

# Hiring problem

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html).

## The hire-assistant scan

Given candidates $x_0, \dots, x_{n-1}$ in a linearly ordered type,
the scan interviews them in order while keeping a current manager, initially none, which counts
as below every candidate. Candidate $i$ is hired exactly when $x_i$ is strictly greater than the
value of the current manager, and then becomes the new manager; ties keep the earlier manager.
The scan returns the zero-based index of the final manager (none for the empty list) and the
list of hired indices in the order they were hired, and its cost is the pair (number of
interviews, number of hires).

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant`, a definition declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant).

## The hire-assistant scan returns the earliest best candidate

For every list
$x_0, \dots, x_{n-1}$ in a linearly ordered type, the manager returned by the hire-assistant scan
is none when the list is empty, and otherwise is the smallest index $i$ such that $x_i$ is a
maximum of the list.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-ret).

## The hire-assistant scan hires exactly the strict prefix maxima

For every list
$x_0, \dots, x_{n-1}$ in a linearly ordered type, the list of indices hired by the hire-assistant
scan, in chronological order, is the increasing list of all indices $i < n$ such that $x_j < x_i$
for every $j < i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_hires`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-hires).

## Cost of the hire-assistant scan

For every list of $n$ candidates in a linearly ordered
type, the cost pair of the hire-assistant scan is $(n, h)$, where $h$ is the length of the list
of hired indices that the scan returns.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-time).

## Hire-assistant scan on no candidates

On the empty list, the hire-assistant scan returns
no manager and an empty list of hires, with cost pair $(0, 0)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-nil).

## Hire-assistant scan on one candidate

For every element $a$ of a linearly ordered type,
on the one-element list $[a]$ the hire-assistant scan returns manager index $0$ and hire list
$[0]$, with cost pair $(1, 1)$: the single candidate is hired regardless of its quality.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-singleton).

## Hire-count bounds for the hire-assistant scan

For every nonempty list of $n$ candidates
in a linearly ordered type, the number of hires $h$ recorded in the cost pair of the
hire-assistant scan satisfies $1 \le h \le n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_hire_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-hire-bounds).

## Strictly increasing input hires every candidate

For every strictly increasing list
$x_0 < x_1 < \dots < x_{n-1}$ in a linearly ordered type, including the empty list, the
hire-assistant scan hires the indices $0, 1, \dots, n - 1$ in that order, and its cost pair is
$(n, n)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_increasing`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistant.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-increasing).

## Expected number of hires under a random permutation

Let $x$ be a list of $n$ pairwise
distinct elements of a linearly ordered type, and rearrange its entries by a uniformly random
permutation of the indices. The expected number of hires, valued in $[0, \infty]$, that the
hire-assistant procedure (interview the entries in order, hiring each one strictly better than
every earlier one) makes on the rearranged list equals $\sum_{i=0}^{n-1} \frac{1}{i+1}$.

## Sources

- CLRS Section 5.2.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_expectedHires`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistantExpected.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistantExpected.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-expected-hires).

## Expected number of hires as a real harmonic sum

Let $x$ be a list of $n$ pairwise
distinct elements of a linearly ordered type, and rearrange its entries by a uniformly random
permutation of the indices. The expected number of hires that the hire-assistant procedure
(interview the entries in order, hiring each one strictly better than every earlier one) makes
on the rearranged list, an element of $[0, \infty]$, converted to a real number, equals
$\sum_{i=0}^{n-1} \frac{1}{i+1}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_expectedHires_toReal`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistantExpected.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistantExpected.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-expected-hires-to-real).

## Expected number of hires is the harmonic number

Let $x$ be a list of $n$ pairwise
distinct elements of a linearly ordered type, and rearrange its entries by a uniformly random
permutation of the indices. The expected number of hires that the hire-assistant procedure
(interview the entries in order, hiring each one strictly better than every earlier one) makes
on the rearranged list, an element of $[0, \infty]$, converted to a real number, equals the
harmonic number $H_n = \sum_{k=1}^{n} \frac{1}{k}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.hireAssistant_expectedHires_toReal_eq_harmonic`, a theorem declared in [CSLibExt/Algorithms/Lean/Selection/HireAssistantExpected.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Selection/HireAssistantExpected.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html#hire-assistant-expected-hires-to-real-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hiring problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/hiring-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/randomized-algorithms/hiring-problem)
