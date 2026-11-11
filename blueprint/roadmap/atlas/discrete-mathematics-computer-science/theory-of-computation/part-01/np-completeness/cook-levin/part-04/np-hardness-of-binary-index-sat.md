---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Hardness.Phi_length, Cslib.Complexity.CookLevin.Hardness.isPolyTime_binConv, Cslib.Complexity.CookLevin.Hardness.satDec_npHard, Cslib.Complexity.CookLevin.Hardness.cook_levin_SAT_np_complete_of_isPolyTime
statement: formalized
proof: formalized
---

# NP-hardness of binary-index SAT

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/np-hardness-of-binary-index-sat/index.html).

## Every clause of the Cook–Levin formula has one slot per variable

Let $E$ be an encoding
of a machine $M$, let $x$ and $Y$ be lists of input symbols of $M$, let $a$ be a symbol of its
output stack, and let $m, T \in \mathbb{N}$. Put $H = m + (T + 1)d + 1$, where $d$ is the window
depth of $M$. Then every clause of the Cook–Levin formula $\Phi(E, x, Y, a, m, T)$ is a dense
clause of length $(T + 1)(A + K H g)$, the number of variables of the layout of $E$ at time bound
$T$ and height $H$, where $A$, $K$ and $g$ are the label/state block size, the number of stacks
and the number of symbol codes of that layout.

Formalized by `Cslib.Complexity.CookLevin.Hardness.Phi_length`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/np-hardness-of-binary-index-sat/index.html#phi-length).

## The dense-to-binary translation is polynomial-time in the canonical encoding

The
translation of bit strings from the dense CNF encoding to the binary-index CNF encoding, as a
function on all bit strings, is polynomial-time computable with respect to the canonical
bitstring encoding of bit lists.

Formalized by `Cslib.Complexity.CookLevin.Hardness.isPolyTime_binConv`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/np-hardness-of-binary-index-sat/index.html#is-poly-time-bin-conv).

## Every NP problem reduces to binary-index CNF-SAT

Every decision problem $L$ in NP has a
polynomial-time many-one reduction to the language of bit strings that encode a satisfiable CNF
formula in the binary-index encoding.

Formalized by `Cslib.Complexity.CookLevin.Hardness.satDec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/np-hardness-of-binary-index-sat/index.html#sat-dec-np-hard).

## Cook–Levin for binary-index CNF-SAT, given a polynomial-time verifier

If the Boolean
result of the SAT verifier, as a function of pairs (formula code, assignment), is computable in
polynomial time, then the language of bit strings that encode a satisfiable CNF formula in the
binary-index encoding is in NP, and every decision problem in NP has a polynomial-time many-one
reduction to it.

Formalized by `Cslib.Complexity.CookLevin.Hardness.cook_levin_SAT_np_complete_of_isPolyTime`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/CookLevin/BinaryHardness.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/np-hardness-of-binary-index-sat/index.html#cook-levin-sat-np-complete-of-is-poly-ti).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: NP-hardness of binary-index SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/np-hardness-of-binary-index-sat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/np-hardness-of-binary-index-sat)
