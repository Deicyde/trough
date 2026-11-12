---
declaration: section
origin: cited
---

# 312. The Grothendieck homotopy hypothesis

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Grothendieck homotopy hypothesis for ∞-groupoids associated with every Grothendieck coherator in the Ara–Henry convention: these algebraic objects recover the homotopy theory of spaces.

## The Grothendieck homotopy hypothesis via elementary expansions

We prove the Grothendieck homotopy hypothesis for every Grothendieck coherator in the Ara–Henry convention: its weak globular infinity-groupoids recover the homotopy theory of spaces. We also resolve Henry's pushout conjecture, showing that elementary expansions preserve components and all homotopy groups of cellular infinity-groupoids.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Grothendieck homotopy hypothesis asks whether algebraic $\infty$-groupoids recover the homotopy theory of spaces. The formalized result is the elementary-expansion theorem used in this approach: for every Grothendieck coherator in the Ara–Henry convention and every boundary-cellular model, attaching an $(n+1)$-disk along its source $n$-face induces a weak equivalence.

The later semi-model structure and full comparison with the homotopy theory of spaces are not included.

## Lean: Elementary-expansion weak equivalence

Stated in [GrothendieckElementaryExpansion.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GrothendieckElementaryExpansion.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem elementary_expansion (C : GlobularTheory.{v}) (hC : C.IsCoherator)
    (X : C.Model) (hX : X.IsCellular) (n : ℕ)
    (a : GlobularTheory.Model.disk C n ⟶ X)
    (Y : C.Model) (i : X ⟶ Y)
    (b : GlobularTheory.Model.disk C (n + 1) ⟶ Y)
    (square : IsPushout a (GlobularTheory.Model.J C n) i b) :
    GlobularTheory.Model.WeakEquivalence hC i
```

Its proof is in [lean/OAI/CategoryTheory/Globular/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/CategoryTheory/Globular/Main.lean) or a file it imports further down, which this chapter does not read.

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/312.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/312.md)
