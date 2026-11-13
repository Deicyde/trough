---
declaration: section
origin: cited
lean: OAI.WeakPureInfiniteness.exact_weaklyPurelyInfinite_individuallyProperlyInfinite_any, OAI.WeakPureInfiniteness.exact_weaklyPurelyInfinite_stronglyPurelyInfinite, OAI.MainGap.Manuscript.individual_to_strong_main
statement: formalized
proof: formalized
---

# 303. Weak pure infiniteness and Cuntz-algebra absorption

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the ordinary-to-strong pure-infiniteness question of Kirchberg and Rørdam for complex $C^{∗}$-algebras. For exact algebras, proper infiniteness of one fixed finite amplification of every positive element also suffices. Consequently, every separable nuclear algebra with this property absorbs $\mathcal O_\infty$, without unitality or simplicity assumptions.

## Weak pure infiniteness and O-infinity absorption

We prove that every complex $C^{∗}$-algebra in which each positive element is properly infinite is strongly purely infinite. This answers the ordinary-to-strong part of Kirchberg–Rørdam's comparison question. For exact algebras, we also prove that proper infiniteness of one fixed finite amplification of every positive element implies proper infiniteness of each positive element. Consequently, every separable nuclear algebra with this fixed-amplification property absorbs $\mathcal O_\infty$, without assumptions of unitality or simplicity.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves that a complex $C^*$-algebra in which every positive element is properly infinite is strongly purely infinite, with the full positive-element diagonalization property. No exactness, nuclearity, unitality, or simplicity assumption is needed for this implication.

For exact algebras, proper infiniteness of one fixed finite amplification of every positive element already implies individual proper infiniteness and strong pure infiniteness.

## Lean: Fixed-amplification pure infiniteness for exact algebras

```lean
theorem exact_weaklyPurelyInfinite_individuallyProperlyInfinite_any
    {A : Type u} [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
    (hA : Exact A) (hW : WeaklyPurelyInfinite A) {a : A} (ha : 0 ≤ a) :
    ProperlyInfinite (diagonalCopies 1 a)
```

Stated in [ExactInfiniteness.lean, line 164](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ExactInfiniteness.lean#L164). Proved in [lean/OAI/Analysis/WeakInfiniteness/UniverseIndividualInfiniteness.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/WeakInfiniteness/UniverseIndividualInfiniteness.lean#L57).

```lean
theorem exact_weaklyPurelyInfinite_stronglyPurelyInfinite
    (A : Type u) [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
    (hExact : Exact A) (hWeak : WeaklyPurelyInfinite A) : StronglyPurelyInfinite A
```

Stated in [ExactInfiniteness.lean, line 170](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ExactInfiniteness.lean#L170). Proved in [lean/OAI/Analysis/WeakInfiniteness/ExactInfiniteness.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/WeakInfiniteness/ExactInfiniteness.lean#L23).

## Lean: Individual proper infiniteness implies strong pure infiniteness

```lean
theorem individual_to_strong_main (hP : PropertyP A) :
    (∀ a b : A, 0 ≤ a → 0 ≤ b → ∀ c : A, ∀ ε : ℝ, 0 < ε →
      ∃ s t : A,
        ‖star s * a * s - a‖ < ε ∧
        ‖star t * b * t - b‖ < ε ∧
        ‖star s * c * t‖ < ε) ∧
    MainGap.StronglyPurelyInfinite A
```

Stated in [IndividualStrongInfiniteness.lean, line 319](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IndividualStrongInfiniteness.lean#L319). Proved in [lean/OAI/Analysis/CStarAlgebra/PureInfiniteness/Main.lean, line 43](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CStarAlgebra/PureInfiniteness/Main.lean#L43).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/303.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/303.md)
