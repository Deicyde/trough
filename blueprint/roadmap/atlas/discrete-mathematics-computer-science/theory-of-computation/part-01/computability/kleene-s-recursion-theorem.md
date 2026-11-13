---
declaration: section
origin: cited
lean: Cslib.Decidability.exists_quine, Cslib.Decidability.exists_dom_eq_singleton_encode
statement: formalized
proof: formalized
---

# Kleene's recursion theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/kleene-s-recursion-theorem/index.html).

## A quine

There is a code $c$ of a partial recursive function on $\mathbb{N}$ that, on
every input $n \in \mathbb{N}$, halts and outputs the number encoding $c$.

Formalized by `Cslib.Decidability.exists_quine`, a theorem declared in [CSLibExt/Computability/Decidability/RecursionTheorem.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RecursionTheorem.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/kleene-s-recursion-theorem/index.html#exists-quine).

## A code that halts exactly on its own number

There is a code $c$ of a partial recursive
function on $\mathbb{N}$ such that, for every $n \in \mathbb{N}$, $c$ halts on input $n$ if and
only if $n$ is the number encoding $c$.

Formalized by `Cslib.Decidability.exists_dom_eq_singleton_encode`, a theorem declared in [CSLibExt/Computability/Decidability/RecursionTheorem.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/RecursionTheorem.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/kleene-s-recursion-theorem/index.html#exists-dom-eq-singleton-encode).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kleene's recursion theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/kleene-s-recursion-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/computability/kleene-s-recursion-theorem)
