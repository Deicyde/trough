---
declaration: section
origin: cited
lean: Cslib.AutomatedReasoning.StringConstraints.levi_of_le
statement: formalized
proof: formalized
---

# String constraints and word equations: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/index.html).

## Length-directed Levi's lemma

Length-directed Levi's lemma: if `u` is no longer than `x`, then
`x` splits as `u ++ w` and the remainders satisfy `v = w ++ y`. The
general form is Mathlib's `List.append_eq_append_iff`, used directly.

Formalized by `Cslib.AutomatedReasoning.StringConstraints.levi_of_le`, a theorem declared in [CSLibExt/AutomatedReasoning/StringConstraints/Levi.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/AutomatedReasoning/StringConstraints/Levi.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/index.html#levi-of-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: String constraints and word equations](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/decision-procedures/string-constraints-and-word-equations)
