---
declaration: section
origin: cited
lean: MetaMathlibExt.vanDerWaerden
statement: formalized
proof: formalized
---

# Van der Waerden-type theorems: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/index.html).

Monochromatic arithmetic progressions: van der Waerden's theorem and van der Waerden numbers (off-diagonal, W(3,k)), short or large-difference progressions, rainbow progressions, descending waves, accessible sets and diffsequences, and progression-free Ramsey sets.

## Van der Waerden's theorem

For all positive integers $r$ and $k$ there is a natural
number $N$ such that for every coloring of $\{1, \dots, N\}$ with $r$ colors there are natural
numbers $a \ge 1$ and $d \ge 1$ with $a + (k - 1)d \le N$ such that each of the $k$ terms
$a, a + d, \dots, a + (k - 1)d$ has the same color as $a$.

Proof: apply the Hales–Jewett theorem to the digit-sum encoding $x \mapsto 1 + \sum_i x_i$
of words over the alphabet $\{0, \dots, k - 1\}$, so that a combinatorial line becomes an
arithmetic progression. This follows the standard derivation in Graham, Rothschild, and
Spencer, *Ramsey Theory*, Section 2.3, from van der Waerden (1927).

## Sources

- https://en.wikipedia.org/wiki/Van_der_Waerden%27s_theorem

Formalized by `MetaMathlibExt.vanDerWaerden`, a theorem declared in [MathlibExt/Combinatorics/Additive/VanDerWaerdenAP.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/VanDerWaerdenAP.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/index.html#van-der-waerden).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van der Waerden-type theorems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems)
