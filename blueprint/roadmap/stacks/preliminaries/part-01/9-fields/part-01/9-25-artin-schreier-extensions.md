---
declaration: section
origin: cited
lean: IsGalois.exists_artinSchreier_of_finrank_eq_char
statement: formalized
proof: formalized
---

# 9.25 Artin-Schreier extensions

Section 9.25 of the Stacks Project, [Tag 09I7](https://stacks.math.columbia.edu/tag/09I7). 1 tag here is carried by 1 declaration of the repository (in StacksCore), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09DY, a lemma

[Tag 09DY](https://stacks.math.columbia.edu/tag/09DY) in the Stacks Project.

**`IsGalois.exists_artinSchreier_of_finrank_eq_char`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/ArtinSchreier.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/ArtinSchreier.lean#L278).

> **Stacks 09DY**.
> Let `F` be a field of characteristic `p > 0` and let `K/F` be a Galois extension of degree `p`.
> Then `K = F(b)` for some `b ∈ K` whose Artin–Schreier expression `b^p - b` lies in `F`.

```lean
theorem IsGalois.exists_artinSchreier_of_finrank_eq_char
    {F K : Type*} [Field F] [Field K] [Algebra F K] [FiniteDimensional F K] [IsGalois F K]
    {p : ℕ} [Fact p.Prime] [CharP F p] (hp : Module.finrank F K = p) :
    ∃ b : K, F⟮b⟯ = ⊤ ∧ b ^ p - b ∈ Set.range (algebraMap F K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.25, Tag 09I7](https://stacks.math.columbia.edu/tag/09I7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
