---
declaration: section
origin: cited
lean: OAI.PureTypeSystem.weak_implies_strong
statement: formalized
proof: formalized
---

# 245. Weak normalization implies strong normalization in pure type systems

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that weak normalization implies strong normalization for every pure type system: if every legal expression in every valid context has a *β*-normal form, every *β*-reduction sequence terminates. This resolves the *β*-Barendregt–Geuvers–Klop conjecture, including nonfunctional rules and open contexts.

## Weak and strong normalization in pure type systems

We prove that every weakly *β*-normalizing pure type system is strongly *β*-normalizing. Both properties quantify over all legal expressions in all valid contexts, and reduction acts inside type annotations. No functionality hypothesis is required. This resolves the *β*-Barendregt–Geuvers–Klop conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the $\beta$-Barendregt–Geuvers–Klop conjecture for pure type systems: if every legal expression in every valid context has some terminating $\beta$-reduction sequence, then every $\beta$-reduction sequence from every such expression terminates. Reduction is allowed inside type annotations, and the specification may have arbitrary sorts and nonfunctional axioms or rules.

## Lean: Weak normalization implies strong normalization in every pure type system

```lean
theorem weak_implies_strong {S : Type u} (P : Specification S)
    (h : SystemWeaklyNormalizing P) : SystemStronglyNormalizing P
```

Stated in [TypeSystemNormalization.lean, line 116](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TypeSystemNormalization.lean#L116). Proved in [lean/OAI/Computability/TypeSystem/Normalization.lean, line 82](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/TypeSystem/Normalization.lean#L82).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/245.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/245.md)
