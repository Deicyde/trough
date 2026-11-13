---
declaration: section
origin: cited
lean: DividedPowers.Extends, DividedPowers.existsUnique_extension, DividedPowers.DividedPowerRing.dividedPowers_extends_of_map_eq_bot_or_isPrincipal_or_flat, DividedPowers.DividedPowerRing.isDPMorphism_extendedDividedPowersOfMapEqBotOrIsPrincipalOrFlat, DividedPowers.isSubDPIdeal_ker, DividedPowers.Quotient.dividedPowers, DividedPowers.Quotient.isDPMorphism, DividedPowers.subDPIdeal_inf_of_quot
statement: formalized
proof: formalized
---

# 23.4 Extending divided powers

Section 23.4 of the Stacks Project, [Tag 07GZ](https://stacks.math.columbia.edu/tag/07GZ). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07H0, a definition

[Tag 07H0](https://stacks.math.columbia.edu/tag/07H0) in the Stacks Project.

**`DividedPowers.Extends`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean#L71).

> A divided power structure `γ` on `I` extends along `f : A →+* B` if the extended ideal
> `I.map f` admits a divided power structure making `f` a divided power morphism.

```lean
public abbrev Extends
    {A B : Type*} [CommSemiring A] [CommSemiring B] {I : Ideal A}
    (γ : _root_.DividedPowers I) (f : A →+* B) : Prop
```

## Tag 07H1, a lemma

[Tag 07H1](https://stacks.math.columbia.edu/tag/07H1) in the Stacks Project.

**`DividedPowers.existsUnique_extension`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean#L79). The attribute's comment: “uniqueness”.

> If a divided power structure extends along a ring homomorphism, the divided power structure
> on the extended ideal making that homomorphism a divided power morphism is unique.

```lean
public lemma existsUnique_extension {A B : Type*} [CommSemiring A] [CommSemiring B]
    {I : Ideal A} (γ : _root_.DividedPowers I) (f : A →+* B)
    (h : Extends γ f) :
    ∃! δ : _root_.DividedPowers (I.map f),
      _root_.DividedPowers.IsDPMorphism γ δ f
```

**`DividedPowers.DividedPowerRing.dividedPowers_extends_of_map_eq_bot_or_isPrincipal_or_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean, line 705](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean#L705). The attribute's comment: “existence”.

> Divided powers extend along a ring homomorphism if the mapped ideal is zero, the source
> ideal is principal, or the homomorphism is flat.

```lean
public theorem DividedPowerRing.dividedPowers_extends_of_map_eq_bot_or_isPrincipal_or_flat
    (A : DividedPowerRing.{u}) {B : Type v} [CommRing B] (f : A →+* B)
    (h : (A.ideal.map f = ⊥) ∨ A.ideal.IsPrincipal ∨ f.Flat) :
    Extends A.dividedPowers f
```

**`DividedPowers.DividedPowerRing.isDPMorphism_extendedDividedPowersOfMapEqBotOrIsPrincipalOrFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean, line 755](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/Existence.lean#L755). The attribute's comment: “existence”.

> The chosen divided powers on the mapped ideal make the original ring homomorphism a divided
> power morphism.

```lean
public theorem
    DividedPowerRing.isDPMorphism_extendedDividedPowersOfMapEqBotOrIsPrincipalOrFlat
    (A : DividedPowerRing.{u}) {B : Type v} [CommRing B] (f : A →+* B)
    (h : (A.ideal.map f = ⊥) ∨ A.ideal.IsPrincipal ∨ f.Flat) :
    _root_.DividedPowers.IsDPMorphism A.dividedPowers
      (DividedPowerRing.extendedDividedPowersOfMapEqBotOrIsPrincipalOrFlat A f h) f
```

## Tag 07H2, a lemma

[Tag 07H2](https://stacks.math.columbia.edu/tag/07H2) in the Stacks Project.

Declarations registered for the tag:

- [`DividedPowers.isSubDPIdeal_ker`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.isSubDPIdeal_ker#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch23.lean#L21) (StacksFrontier): “(1) Ker(φ) ∩ I is preserved by the γₙ, n ≥ 1”.
- [`DividedPowers.Quotient.dividedPowers`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.Quotient.dividedPowers#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch23.lean#L22) (StacksFrontier): “(2) (a) => (b): the divided power structure on I(A/𝔞)”.
- [`DividedPowers.Quotient.isDPMorphism`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.Quotient.isDPMorphism#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch23.lean#L24) (StacksFrontier): “(2) (a) => (b): A → A/𝔞 is a divided power homomorphism for it”.
- [`DividedPowers.subDPIdeal_inf_of_quot`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.subDPIdeal_inf_of_quot#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch23.lean#L26) (StacksFrontier): “(2) (b) => (a): the sub-dp-ideal with carrier 𝔞 ⊓ I (by definition)”.
- [`DividedPowers.span_isSubDPIdeal_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.span_isSubDPIdeal_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch23.lean#L28) (StacksFrontier): “(2) (a) <=> (c), for I' = span S with S ⊆ I”.

## Tag 07H3, a lemma

[Tag 07H3](https://stacks.math.columbia.edu/tag/07H3) in the Stacks Project.

Declarations registered for the tag:

- [`DividedPowers.SubDPIdeal.span`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.SubDPIdeal.span#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch23.lean#L29) (StacksFrontier): “the smallest sub-dp-ideal containing E (the infimum of those containing E)”.
- [`DividedPowers.SubDPIdeal.span_carrier_eq_dpow_span`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.SubDPIdeal.span_carrier_eq_dpow_span#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch23.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch23.lean#L31) (StacksFrontier): “its ideal is generated by the γₙ(f), n ≥ 1, f ∈ E”.

## Tag 07KD, a lemma

[Tag 07KD](https://stacks.math.columbia.edu/tag/07KD) in the Stacks Project.

**`DividedPowers.completedDividedPowers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/CompletedDividedPowers.lean, line 583](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/CompletedDividedPowers.lean#L583). The attribute's comment: “part (3), extension”.

> Part (3), extension: the divided powers on `I` extend to its completed
> ideal.  The subtype records the naturality on the dense image of `I`.

```lean
public noncomputable def completedDividedPowers
    (hp : IsNilpotent (Ideal.Quotient.mk I (p : A))) :
    { δ : DividedPowers (completionIdeal I p hp) //
      ∀ (n : ℕ) (x : A) (_hx : x ∈ I) (xhat : completionIdeal I p hp),
        (xhat : AdicCompletion (pAdicIdeal (A := A) p) A) =
            algebraMap A (AdicCompletion (pAdicIdeal (A := A) p) A) x →
          δ.dpow n xhat =
            algebraMap A (AdicCompletion (pAdicIdeal (A := A) p) A) (γ.dpow n x) }
```

**`DividedPowers.eventually_isDividedPowerCompletionLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/CompletedDividedPowers.lean, line 741](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/CompletedDividedPowers.lean#L741). The attribute's comment: “part (4)”.

> Part (4): over `ℤ_(p)`, sufficiently high powers of `(p)` are stable under
> the divided powers and the completed divided power ring has the inverse-limit
> universal property for the resulting quotient divided power rings.

```lean
public theorem eventually_isDividedPowerCompletionLimit [Fact p.Prime]
    [Algebra (IntegersAtPrime p) A]
    (hp : IsNilpotent (Ideal.Quotient.mk I (p : A))) :
    ∃ N, ∃ hlevel : ∀ e, N ≤ e →
      (pAdicIdeal (A := A) p ^ e ≤ I) ∧
        γ.IsSubDPIdeal (pAdicIdeal (A := A) p ^ e),
      IsDividedPowerCompletionLimit I γ p hp N hlevel
```

**`DividedPowers.completionToQuotient_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/Completion.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/Completion.lean#L178). The attribute's comment: “part (1)”.

> Part (1): the `p`-adic completion maps onto the quotient by the divided
> power ideal.

```lean
public theorem completionToQuotient_surjective
    (hp : IsNilpotent (Ideal.Quotient.mk I (p : A))) :
    Function.Surjective (completionToQuotient I p hp)
```

**`DividedPowers.completionIdealEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/Completion.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/Completion.lean#L333). The attribute's comment: “part (2)”.

> Part (2): the completion of `I`, mapped into the completion of `A`, is
> canonically the kernel of the map to `A/I`.

```lean
public noncomputable def completionIdealEquiv
    (hp : IsNilpotent (Ideal.Quotient.mk I (p : A))) :
    { e : AdicCompletion (pAdicIdeal (A := A) p) I ≃ₗ[
          AdicCompletion (pAdicIdeal (A := A) p) A] completionIdeal I p hp //
      ∀ x, ((e x : completionIdeal I p hp) :
        AdicCompletion (pAdicIdeal (A := A) p) A) =
          AdicCompletion.map (pAdicIdeal (A := A) p) I.subtype x }
```

**`DividedPowers.dpow_pAdic_continuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Extend/Completion.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Extend/Completion.lean#L368). The attribute's comment: “part (3), continuity”.

> Part (3), continuity: changing an element of `I` by an element of
> `p^e I` changes every divided power by an element of `p^e I`.

```lean
public theorem dpow_pAdic_continuous (n e : ℕ) {x y : A}
    (hx : x ∈ I) (hy : y ∈ I) :
    γ.dpow n (x + (p : A) ^ e * y) - γ.dpow n x ∈
      pAdicIdeal (A := A) p ^ e • (I : Submodule A A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 23.4, Tag 07GZ](https://stacks.math.columbia.edu/tag/07GZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
