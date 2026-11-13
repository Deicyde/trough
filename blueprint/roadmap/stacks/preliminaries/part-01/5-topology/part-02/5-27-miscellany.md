---
declaration: section
origin: cited
lean: locallyCompactSpace_and_isRetrocompact_and_hasCofinalCompactRefinements, IsIsolatedPoint
statement: formalized
proof: formalized
---

# 5.27 Miscellany

Section 5.27 of the Stacks Project, [Tag 0067](https://stacks.math.columbia.edu/tag/0067). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0069, a lemma

[Tag 0069](https://stacks.math.columbia.edu/tag/0069) in the Stacks Project.

**`locallyCompactSpace_and_isRetrocompact_and_hasCofinalCompactRefinements`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Bases/QuasiCompactOpens.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Bases/QuasiCompactOpens.lean#L114). References: EGA 0 (9.1.6), “second conjunct”.

> **Stacks 0069.** Under hypotheses (H1) and (H2), `X` is locally quasi-compact, every
> quasi-compact open of `X` is retrocompact, and every quasi-compact open of `X` has a cofinal system
> of finite open coverings by quasi-compact opens with quasi-compact pairwise intersections.

```lean
theorem locallyCompactSpace_and_isRetrocompact_and_hasCofinalCompactRefinements
    (h1 : PrespectralSpace X) (h2 : QuasiSeparatedSpace X) :
    LocallyCompactSpace X ∧
    (∀ {U : Set X}, IsOpen U → IsCompact U → IsRetrocompact U) ∧
    (∀ {U : Set X}, IsOpen U → IsCompact U → HasCofinalCompactRefinements U)
```

## Tag 06RM, a definition

[Tag 06RM](https://stacks.math.columbia.edu/tag/06RM) in the Stacks Project.

**`IsIsolatedPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Separation/IsolatedPoint.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Separation/IsolatedPoint.lean#L20).

> **Stacks 06RM.** A point `x` of a topological space `X` is *isolated* if `{x}` is open in
> `X`.

```lean
def IsIsolatedPoint {X : Type*} [TopologicalSpace X] (x : X) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.27, Tag 0067](https://stacks.math.columbia.edu/tag/0067)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
