---
declaration: section
origin: cited
lean: Stacks.Examples.CurveFamilyNotScheme.not_exists_scheme_of_no_dominating_closed_avoiding
statement: formalized
proof: formalized
---

# 110.69 A family of curves whose total space is not a scheme

Section 110.69 of the Stacks Project, [Tag 0D5D](https://stacks.math.columbia.edu/tag/0D5D). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D5E, a lemma

[Tag 0D5E](https://stacks.math.columbia.edu/tag/0D5E) in the Stacks Project.

**`Stacks.Examples.CurveFamilyNotScheme.not_exists_scheme_of_no_dominating_closed_avoiding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/CurveFamilyNotScheme.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/CurveFamilyNotScheme.lean#L197). The attribute's comment: “the obstruction: no scheme carries the geometry of the construction, conditional on Artin's contraction theorem and on the choice of the point on the central fibre, whose outputs are the hypotheses”.

> **Stacks 0D5E.** There exists a field `k` and a family of curves `X → A¹_k` such that `X` is
> not a scheme.
>
> What is proved is the obstruction: no *scheme* carries the geometry that the construction
> produces. Explicitly, there is no scheme `X` with a proper morphism `f : X ⟶ S` to an affine base
> whose fibres are all infinite, together with a point `x` of `X` such that no closed subset of `X`
> avoiding `x` surjects onto `S`.
>
> The total space of the source's family satisfies the three hypotheses with `S = A¹_k`: it is
> proper over the affine line with one-dimensional, hence infinite, fibres, and the point `x` to
> which the strict transform of the central fibre is contracted is avoided by no dominating closed
> subset, because such a subset would push down to a proper closed subscheme of the cubic surface
> `Y` dominating the affine line and meeting `Y₀` only in the chosen point `y`. So the total space
> is not a scheme.
>
> What is *not* proved is that the family exists. Its construction needs Artin's contraction
> theorem for algebraic spaces, which this library does not have, and the point `y` on the Fermat
> cubic is chosen by a countability argument against the Picard group of the rational surface `Y`;
> both are inputs rather than conclusions here, and what they deliver is precisely the third
> hypothesis below.

```lean
theorem not_exists_scheme_of_no_dominating_closed_avoiding (S : Scheme.{u}) [IsAffine S] :
    ¬ ∃ (X : Scheme.{u}) (f : X ⟶ S) (_ : IsProper f) (x : X),
        (∀ s : S, ¬ (f ⁻¹' {s}).Finite) ∧
          ∀ T : Set X, IsClosed T → x ∉ T → ∃ s : S, ∀ y ∈ T, f y ≠ s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.69, Tag 0D5D](https://stacks.math.columbia.edu/tag/0D5D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
