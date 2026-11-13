---
declaration: section
origin: cited
lean: Submodule.IsDirectSumDevissage, Submodule.IsKaplanskyDevissage, devissage_iso, Submodule.exists_sSupIndep_countable_span_iff_exists_isKaplanskyDevissage, Submodule.exists_sSupIndep_countable_span_of_isCompl, Submodule.exists_sSupIndep_countable_span_projective_of_projective
statement: formalized
proof: formalized
---

# 10.84 Transfinite dévissage of modules

Section 10.84 of the Stacks Project, [Tag 058T](https://stacks.math.columbia.edu/tag/058T). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 058U, a definition

[Tag 058U](https://stacks.math.columbia.edu/tag/058U) in the Stacks Project.

**`Submodule.IsDirectSumDevissage`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Devissage.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Devissage.lean#L290). The attribute's comment: “direct sum devissage”.

> A *direct sum dévissage* of an `R`-module `M` is an increasing family `N` of submodules of `M`,
> indexed by the ordinals `α < s`, with `N 0 = 0`, with union `M`, continuous at limit ordinals, and
> with `N α` a direct summand of `N (α + 1)` whenever `α + 1 < s`.

```lean
public structure IsDirectSumDevissage (s : Ordinal.{w}) (N : Ordinal.{w} → Submodule R M) :
    Prop
```

**`Submodule.IsKaplanskyDevissage`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Devissage.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Devissage.lean#L309). The attribute's comment: “Kaplansky devissage”.

> A *Kaplansky dévissage* of an `R`-module `M` is a direct sum dévissage all of whose quotients
> `N (α + 1) / N α` are countably generated, which is to say that `N (α + 1)` is generated over `N α`
> by countably many elements of `M`.

```lean
public structure IsKaplanskyDevissage (s : Ordinal.{w}) (N : Ordinal.{w} → Submodule R M) : Prop
    extends IsDirectSumDevissage s N
```

## Tag 058V, a lemma

[Tag 058V](https://stacks.math.columbia.edu/tag/058V) in the Stacks Project.

**`devissage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Devissage.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Devissage.lean#L121).

> **Stacks Tag 058V (Lemma 10.84.2).** Given a direct sum dévissage of `N`,
> the module `N` is isomorphic to the direct sum of the successive quotients
> `M_{α+1} / M_α` over all ordinals `α` with `α + 1 < S`.
>
> Here the `α`-th summand `M_{α+1}/M_α` is realized as the quotient of the
> submodule `M (Order.succ α)` of `N` by the image of `M α` inside it
> (`(M α).submoduleOf (M (Order.succ α))`, which is `M α ⊓ M (succ α) = M α`
> viewed as a submodule of `↥(M (succ α))`).

```lean
theorem devissage_iso (D : DirectSumDevissage.{u} R N) :
    Nonempty (N ≃ₗ[R] DirectSum {α : Ordinal.{u} // Order.succ α < D.S}
      (fun a => (D.M (Order.succ a.1)) ⧸ (D.M a.1).submoduleOf (D.M (Order.succ a.1))))
```

## Tag 058W, a lemma

[Tag 058W](https://stacks.math.columbia.edu/tag/058W) in the Stacks Project.

**`Submodule.exists_sSupIndep_countable_span_iff_exists_isKaplanskyDevissage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Devissage.lean, line 604](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Devissage.lean#L604). The attribute's comment: “Countable generation written as a countable spanning set, and the direct sum decomposition internally, as an independent set of submodules of `M` with supremum `⊤`.”.

> **Stacks 058W.** Let `M` be a module over a ring `R`. Then `M` is a direct sum of countably
> generated `R`-modules — that is, `M` is the internal direct sum of an independent set of countably
> generated submodules — if and only if `M` admits a Kaplansky dévissage.

```lean
public theorem exists_sSupIndep_countable_span_iff_exists_isKaplanskyDevissage
    (R : Type v) (M : Type u) [Ring R] [AddCommGroup M] [Module R M] :
    (∃ S : Set (Submodule R M), sSupIndep S ∧ sSup S = ⊤ ∧
        ∀ N ∈ S, ∃ t : Set M, t.Countable ∧ span R t = N) ↔
      ∃ (s : Ordinal.{u}) (N : Ordinal.{u} → Submodule R M),
        IsKaplanskyDevissage s N
```

## Tag 058X, a theorem

[Tag 058X](https://stacks.math.columbia.edu/tag/058X) in the Stacks Project.

**`Submodule.exists_sSupIndep_countable_span_of_isCompl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/DirectSum/CountablyGenerated.lean, line 557](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/DirectSum/CountablyGenerated.lean#L557). The attribute's comment: “Being a direct sum of countably generated modules written internally, as in 058W: an independent set of submodules with supremum `⊤`, each spanned by a countable set. `P` is a direct summand of `M` in the sense of a complement in the submodule lattice of `M`.”.

> **Stacks 058X.** Let `M` be a module over a ring `R` which is a direct sum of countably
> generated `R`-modules — that is, `M` is the internal direct sum of an independent set of countably
> generated submodules. If `P` is a direct summand of `M`, with complement `Q`, then `P` is also a
> direct sum of countably generated `R`-modules.

```lean
public theorem exists_sSupIndep_countable_span_of_isCompl {R : Type*} {M : Type*} [Ring R]
    [AddCommGroup M] [Module R M]
    (hM : ∃ S : Set (Submodule R M), sSupIndep S ∧ sSup S = ⊤ ∧
      ∀ N ∈ S, ∃ t : Set M, t.Countable ∧ span R t = N)
    (P Q : Submodule R M) (hPQ : IsCompl P Q) :
    ∃ S : Set (Submodule R ↥P), sSupIndep S ∧ sSup S = ⊤ ∧
      ∀ N ∈ S, ∃ t : Set ↥P, t.Countable ∧ span R t = N
```

## Tag 058Y, a theorem

[Tag 058Y](https://stacks.math.columbia.edu/tag/058Y) in the Stacks Project.

**`Submodule.exists_sSupIndep_countable_span_projective_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/DirectSum/ProjectiveCountablyGenerated.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/DirectSum/ProjectiveCountablyGenerated.lean#L247). The attribute's comment: “Being a direct sum of countably generated projective modules is written internally, as in 058W and 058X: an independent set of submodules with supremum `⊤`, each spanned by a countable set and each projective. Countable generation is a countable spanning set.”.

> Let `M` be a projective module over a ring `R`. Then `M` is a direct sum of countably generated
> projective `R`-modules: there is an independent set of submodules of `M` with supremum `⊤`, each
> spanned by a countable set and each projective over `R`.

```lean
public theorem exists_sSupIndep_countable_span_projective_of_projective {R : Type*} {M : Type*}
    [Ring R] [AddCommGroup M] [Module R M] [Module.Projective R M] :
    ∃ S : Set (Submodule R M), sSupIndep S ∧ sSup S = ⊤ ∧
      ∀ N ∈ S, (∃ t : Set M, t.Countable ∧ span R t = N) ∧ Module.Projective R ↥N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.84, Tag 058T](https://stacks.math.columbia.edu/tag/058T)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
