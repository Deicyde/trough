---
declaration: section
origin: cited
lean: IsGlobalCompleteIntersection, IsLocalCompleteIntersection, isGlobalCompleteIntersection_localization, isLocalCompleteIntersection_localization, IsCompleteIntersection.isMaximalCohenMacaulay, IsLocalCompleteIntersection.isMaximalCohenMacaulay_localization, Algebra.Generators.tfae_isGlobalCompleteIntersection_away, Algebra.Generators.spanFinrank_ker_map_le_iff_exists_isRegular
statement: formalized
proof: formalized
---

# 10.135 Local complete intersections

Section 10.135 of the Stacks Project, [Tag 00S8](https://stacks.math.columbia.edu/tag/00S8). 12 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00S9, a definition

[Tag 00S9](https://stacks.math.columbia.edu/tag/00S9) in the Stacks Project.

**`IsGlobalCompleteIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Defs.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Defs.lean#L93). The attribute's comment: “(1)”.

> Let `k` be a field. A `k`-algebra `S` is a *global complete intersection over `k`* if either
> `S` is the zero ring (`Subsingleton S`), or there are `n, c ≥ 0` and an isomorphism of
> `k`-algebras `S ≃ₐ[k] k[x_1, …, x_n]/(f_1, …, f_c)` with `dim S = n - c`.
>
> Here `k[x_1, …, x_n]` is `MvPolynomial (Fin n) k`, the relations `(f_1, …, f_c)` are the ideal
> `Ideal.span (Set.range f)` for `f : Fin c → MvPolynomial (Fin n) k`, and the dimension condition
> is `c ≤ n` together with `ringKrullDim S = ((n - c : ℕ) : WithBot ℕ∞)`.

```lean
public def IsGlobalCompleteIntersection (k : Type*) [Field k] (S : Type*) [CommRing S]
    [Algebra k S] : Prop
```

**`IsLocalCompleteIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Defs.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Defs.lean#L107). The attribute's comment: “(2)”. References: EGA IV (19.3.6); SGA 6 0 (3.2), “special case”.

> Let `k` be a field. A `k`-algebra `S` is a *local complete intersection over `k`* if there is
> a set `s ⊆ S` whose standard opens `D(g)` cover `Spec S`, and such that `S_g = Localization.Away g`
> is a global complete intersection over `k` for every `g ∈ s`.
>
> The covering condition is recorded algebraically as `Ideal.span s = ⊤`;
> `localCompleteIntersection_cover_iff` is its equivalence with `⨆ g ∈ s, D(g) = ⊤`.

```lean
public def IsLocalCompleteIntersection (k : Type*) [Field k] (S : Type*) [CommRing S]
    [Algebra k S] : Prop
```

## Tag 00SA, a lemma

[Tag 00SA](https://stacks.math.columbia.edu/tag/00SA) in the Stacks Project.

Declarations registered for the tag:

- [`isGlobalCompleteIntersection_localization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Basic.lean#L316), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/CompleteIntersection/Criteria.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Criteria.lean#L176) (StacksFrontier): “part (1): a localization of a global complete intersection over a field is a global complete intersection over that field”.
- [`isLocalCompleteIntersection_localization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Basic.lean#L333), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/CompleteIntersection/Criteria.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Criteria.lean#L179) (StacksFrontier): “part (2): a localization of a local complete intersection over a field is a local complete intersection over that field”.

## Tag 00SB, a lemma

[Tag 00SB](https://stacks.math.columbia.edu/tag/00SB) in the Stacks Project.

**`IsCompleteIntersection.isMaximalCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Local.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Local.lean#L232). The attribute's comment: “The pointwise half of the lemma: Cohen-Macaulayness of a single complete intersection local ring over `k`, stated as `Module.IsMaximalCohenMacaulay` over itself as in 00ND.”. References: EGA 0 (17.1.3), “Cohen–Macaulay”.

> **A complete intersection over a field is a Cohen–Macaulay local ring.** Writing the ring as
> `R/(f_1, …, f_c)` with `R` regular local and `f_1, …, f_c` a regular sequence, `R` is
> Cohen–Macaulay (Lemma 00NQ) and the quotient of a Cohen–Macaulay local ring by a regular sequence
> is again Cohen–Macaulay (Proposition 02JN).

```lean
theorem IsCompleteIntersection.isMaximalCohenMacaulay {k : Type*} [Field k] {A : Type*}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A] [Algebra k A]
    (h : IsCompleteIntersection k A) : Module.IsMaximalCohenMacaulay A A
```

**`IsLocalCompleteIntersection.isMaximalCohenMacaulay_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Local.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Local.lean#L252). The attribute's comment: “Cohen-Macaulayness of the Noetherian ring `S` (Definition 00NC) is spelled out as a condition on its localizations at primes, each being `Module.IsMaximalCohenMacaulay` over itself, as in 00ND. The finite type hypothesis is omitted, being a consequence of `IsLocalCompleteIntersection`. See the module docstring.”.

> **A local complete intersection over a field is Cohen–Macaulay.** Let `k` be a field and let
> `S` be a local complete intersection over `k`. Then every local ring `S_𝔮` of `S` at a prime is a
> Cohen–Macaulay local ring, `depth(S_𝔮) = dim(S_𝔮)`.

```lean
theorem IsLocalCompleteIntersection.isMaximalCohenMacaulay_localization
    {k : Type*} [Field k] {S : Type*} [CommRing S] [Algebra k S]
    (h : IsLocalCompleteIntersection k S) (q : Ideal S) [q.IsPrime] :
    Module.IsMaximalCohenMacaulay (Localization.AtPrime q) (Localization.AtPrime q)
```

## Tag 00SC, a lemma

[Tag 00SC](https://stacks.math.columbia.edu/tag/00SC) in the Stacks Project.

**`Algebra.Generators.tfae_isGlobalCompleteIntersection_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/AtPrime/Criterion.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/AtPrime/Criterion.lean#L495). The attribute's comment: “Items (1)-(5) are the five entries of the `List.TFAE`, in order. The source's `c`, defined there as `height 𝔮' - height 𝔮`, is the hypothesis `height 𝔮' = height 𝔮 + c`, the additive form (see the module docstring); the source's parenthetical `dim_𝔮(S) = n - c` is a consequence of it, by Stacks 00P2. Items (3) and (4) are stated for the conormal module of `I_A = I_{𝔮'}` over `A/I_A` rather than for `(I/I²)_𝔮` over `S_𝔮`; the two agree under the canonical identification of `A/I_A` with `S_𝔮`, localization being flat. The closing assertion of the lemma is the second conjunct of `Algebra.Generators.spanFinrank_ker_map_le_iff_exists_isRegular`, which carries this tag as well.”.

> **The complete intersection criterion at a prime.** Let `k` be a field, let `S = k[x_i]/I` be a
> presented `k`-algebra with finitely many variables, let `q` be a prime of `S`, let `q'` be the
> corresponding prime of `k[x_i]` and let `c` be the codimension, `height q' = height q + c`. Write
> `A = k[x_i]_{q'}` and `I_A = I_{q'}`. Then the following are equivalent:
>
> 1. there is a `g ∈ S`, `g ∉ q`, such that `S_g` is a global complete intersection over `k`;
> 2. the ideal `I_A` can be generated by `c` elements;
> 3. the conormal module `I_A/I_A²` can be generated by `c` elements over `A/I_A`;
> 4. the conormal module `I_A/I_A²` is a free `A/I_A`-module of rank `c`;
> 5. the ideal `I_A` can be generated by a regular sequence in the regular local ring `A`.
>
> Items (3) and (4) are stated for the conormal module of `I_A` over `A/I_A`, which agrees with
> `(I/I²)_q` over `S_q`: `A/I_A` is the localization `S_q` (this is
> `ringKrullDim_quotient_map_ker_eq_height`), and `I_A/I_A²` is `(I/I²)_q`, localization being flat.
>
> The closing assertion of the lemma, that any `c` elements of `I_A` generating `I_A/q'I_A` form a
> regular sequence in `A`, is the second conjunct of
> `Algebra.Generators.spanFinrank_ker_map_le_iff_exists_isRegular`.

```lean
theorem Algebra.Generators.tfae_isGlobalCompleteIntersection_away
    (k : Type u) [Field k] (S : Type v) [CommRing S] [Algebra k S]
    {ι : Type w} [Finite ι] (P : Algebra.Generators k S ι)
    (q : Ideal S) [q.IsPrime] (c : ℕ)
    (hc : (q.comap (algebraMap P.Ring S)).height = q.height + c)
    (A : Type*) [CommRing A] [Algebra P.Ring A]
    [IsLocalization.AtPrime A (q.comap (algebraMap P.Ring S))] :
    List.TFAE
      [∃ g ∉ q, IsGlobalCompleteIntersection k (Localization.Away g),
        Submodule.spanFinrank (P.ker.map (algebraMap P.Ring A)) ≤ c,
        (⊤ : Submodule (A ⧸ P.ker.map (algebraMap P.Ring A))
            (P.ker.map (algebraMap P.Ring A)).Cotangent).spanFinrank ≤ c,
        Module.Free (A ⧸ P.ker.map (algebraMap P.Ring A))
              (P.ker.map (algebraMap P.Ring A)).Cotangent ∧
          Module.finrank (A ⧸ P.ker.map (algebraMap P.Ring A))
            (P.ker.map (algebraMap P.Ring A)).Cotangent = c,
        ∃ rs : List A, IsRegular A rs ∧
          Ideal.ofList rs = P.ker.map (algebraMap P.Ring A)]
```

**`Algebra.Generators.spanFinrank_ker_map_le_iff_exists_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/AtPrime/LocalCriterion.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/AtPrime/LocalCriterion.lean#L510). The attribute's comment: “The equivalence of items (2) and (5) is the first conjunct, and the closing assertion of the lemma — that any `c` elements of `I_{𝔮'}` generating `I_{𝔮'}/𝔮'I_{𝔮'}` form a regular sequence — is the second. The five equivalent conditions themselves are `Algebra.Generators.tfae_isGlobalCompleteIntersection_away`, which carries this tag as well; this declaration is on the covering set for the closing assertion.”.

> **The equivalence of items (2) and (5), together with the closing assertion.**
>
> Let `k` be a field, let `S = k[x_i]/I` be a presented `k`-algebra with finitely many variables, let
> `q` be a prime of `S`, let `q'` be the corresponding prime of `k[x_i]`, and let `c` be the
> codimension, `height q' = height q + c`. Then the ideal `I_{q'}` of `A = k[x_i]_{q'}` can be
> generated by `c` elements if and only if it can be generated by a regular sequence; and any `c`
> elements of `I_{q'}` generating `I_{q'}/q'I_{q'}` form a regular sequence.

```lean
theorem Algebra.Generators.spanFinrank_ker_map_le_iff_exists_isRegular
    (k : Type u) [Field k] (S : Type v) [CommRing S] [Algebra k S]
    {ι : Type w} [Finite ι] (P : Algebra.Generators k S ι)
    (q : Ideal S) [q.IsPrime] (c : ℕ)
    (hc : (q.comap (algebraMap P.Ring S)).height = q.height + c)
    (A : Type*) [CommRing A] [Algebra P.Ring A]
    [IsLocalization.AtPrime A (q.comap (algebraMap P.Ring S))] :
    (Submodule.spanFinrank (P.ker.map (algebraMap P.Ring A)) ≤ c ↔
        ∃ rs : List A, IsRegular A rs ∧
          Ideal.ofList rs = P.ker.map (algebraMap P.Ring A)) ∧
      ∀ rs : List A, rs.length = c →
        Ideal.ofList rs ⊔ (q.comap (algebraMap P.Ring S)).map (algebraMap P.Ring A) *
            P.ker.map (algebraMap P.Ring A) = P.ker.map (algebraMap P.Ring A) →
          IsRegular A rs
```

## Tag 00SD, a definition

[Tag 00SD](https://stacks.math.columbia.edu/tag/00SD) in the Stacks Project.

**`IsCompleteIntersectionLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Criteria.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Criteria.lean#L86).

> A `k`-algebra `S` is a *complete intersection over `k`* if there exist a `k`-algebra `R` and
> a list `f = f₁, …, f_c` of elements of `R` such that
>
> * `R` is a regular local ring,
> * `R` is essentially of finite type over `k`,
> * every `fᵢ` lies in the maximal ideal of `R`,
> * `f₁, …, f_c` is a regular sequence in `R`, and
> * `S ≅ R/(f₁, …, f_c)` as `k`-algebras.
>
> The source states this for a local `k`-algebra `S` essentially of finite type over `k`; both
> hypotheses are consequences here, see `IsCompleteIntersectionLocalRing.isLocalRing` and
> `IsCompleteIntersectionLocalRing.essFiniteType`. The length `c` of `f` is unconstrained, and is
> forced to be the codimension `dim R - dim S` by
> `IsCompleteIntersectionLocalRing.exists_witness`.

```lean
def IsCompleteIntersectionLocalRing (k : Type u) [Field k] (S : Type v) [CommRing S]
    [Algebra k S] : Prop
```

**`IsCompleteIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Defs.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Defs.lean#L168). The attribute's comment: “Items (1)-(4) are the four clauses of the body, in order. The source's condition `f_1, …, f_c ∈ 𝔪_R` is not stated separately: over the local ring `R` it is equivalent, given item (3), to the nonvanishing of `R/(f_1, …, f_c)` that Mathlib's `RingTheory.Sequence.IsRegular` already carries. The source's hypotheses that `S` be local and essentially of finite type over `k` are omitted, both being consequences of the existence of `R`, as with the finite type hypothesis in Definition 00S9. The witness `R` is quantified in the universe of `k`. See the module docstring.”.

> Let `k` be a field. A `k`-algebra `S` is a *complete intersection over `k`* if there are a
> regular local `k`-algebra `R`, essentially of finite type over `k`, and a regular sequence
> `f_1, …, f_c` in `R` such that `S ≃ₐ[k] R/(f_1, …, f_c)`. The condition `f_1, …, f_c ∈ 𝔪_R` is
> contained in `RingTheory.Sequence.IsRegular`, which asks the quotient `R/(f_1, …, f_c)` to be
> nonzero.

```lean
public def IsCompleteIntersection (k : Type u) [Field k] (S : Type v) [CommRing S]
    [Algebra k S] : Prop
```

## Tag 00SE, a lemma

[Tag 00SE](https://stacks.math.columbia.edu/tag/00SE) in the Stacks Project.

**`IsRegularLocalRing.exists_isRegular_ker_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Basic.lean, line 2066](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RegularLocalRing/Basic.lean#L2066). The attribute's comment: “Items (1)-(4) are the four items of the list, in the source's order. `Ker(A → C)` is `RingHom.ker (g.comp f)`. `Generated by dim A - dim C elements` is the equality `ringKrullDim C + (RingHom.ker (g.comp f)).spanFinrank = ringKrullDim A`: subtraction in `WithBot ℕ∞` is truncated, while the inequality `≤` always holds here by Krull's height theorem, so the equality says exactly that the minimal number of generators attains `dim A - dim C`. The source's hypotheses that the maps be local homomorphisms and that `C` be local are omitted, all three being consequences of surjectivity. See the module docstring.”.

> **Stacks 00SE.** Let `A → B → C` be surjective local ring homomorphisms with `A` and `B`
> regular local rings. Then the following are equivalent: `Ker(A → C)` is generated by a regular
> sequence; `Ker(A → C)` is generated by `dim A - dim C` elements; `Ker(B → C)` is generated by a
> regular sequence; `Ker(B → C)` is generated by `dim B - dim C` elements.
>
> Being generated by `n` elements is `Submodule.spanFinrank ≤ n`, stated here in the equivalent
> additive form `dim C + spanFinrank (Ker) = dim A` (respectively `= dim B`), since the reverse
> inequality is Krull's height theorem. See the module docstring.

```lean
public theorem IsRegularLocalRing.exists_isRegular_ker_tfae
    {A B C : Type*} [CommRing A] [CommRing B] [CommRing C]
    [IsRegularLocalRing A] [IsRegularLocalRing B] [Nontrivial C]
    {f : A →+* B} {g : B →+* C} (hf : Function.Surjective f) (hg : Function.Surjective g) :
    List.TFAE
      [∃ rs : List A, RingTheory.Sequence.IsRegular A rs ∧
          Ideal.ofList rs = RingHom.ker (g.comp f),
        ringKrullDim C + (RingHom.ker (g.comp f)).spanFinrank = ringKrullDim A,
        ∃ rs : List B, RingTheory.Sequence.IsRegular B rs ∧ Ideal.ofList rs = RingHom.ker g,
        ringKrullDim C + (RingHom.ker g).spanFinrank = ringKrullDim B]
```

## Tag 00SF, a lemma

[Tag 00SF](https://stacks.math.columbia.edu/tag/00SF) in the Stacks Project.

**`IsCompleteIntersection.tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/LocalRing.lean, line 896](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/LocalRing.lean#L896). The attribute's comment: “Items (1)-(5) are the five items of the list, in the source's order. `Essentially of finite presentation over k` is `Algebra.EssFiniteType k R`, the two notions agreeing over a field; the source's proof states item (2) with `essentially of finite type` as well. `Generated by dim R - dim S elements` is `ringKrullDim S + (RingHom.ker f).spanFinrank = ringKrullDim R`, the reading of Lemma 00SE: subtraction in `WithBot ℕ∞` is truncated while the inequality `≥` holds unconditionally, so the equality says the minimal number of generators attains `dim R - dim S`. In items (4) and (5) the isomorphism `S ≅ A_𝔞` is stated abstractly, as `IsLocalization.AtPrime S a` for an `A`-algebra structure on `S` compatible with `k`. Item (2) quantifies over rings in `Type (max u w)` for a universe parameter `w`: that asserts it in every universe and still lets it be instantiated at the localization `k[x_1, …, x_n]_𝔮` of the source's proof of (2) ⇒ (1), which a free `Type w` would not. The existential items (3)-(5) put their witnesses in the universe of `k`, where the source's are. The hypothesis that the surjections be local ring homomorphisms is omitted, being a consequence of surjectivity. See the module docstring.”. References: EGA IV (19.3.2), “ess. f.t. over a field”.

> Let `k` be a field and let `S` be a local `k`-algebra essentially of finite
> type over `k`. The following are equivalent: `S` is a complete intersection over `k`; for every
> surjection `f : R →ₐ[k] S` with `R` a regular local `k`-algebra essentially of finite type over
> `k` the ideal `Ker f` is generated by a regular sequence; for some such surjection `Ker f` is
> generated by `dim R - dim S` elements; `S` is a localization of a global complete intersection
> over `k` at a prime; and `S` is a localization of a local complete intersection over `k` at a
> prime.
>
> `Generated by dim R - dim S elements` is the additive equality
> `dim S + spanFinrank (Ker f) = dim R`, and items (4) and (5) exhibit `S` as a localization by an
> instance rather than by an isomorphism with `Localization.AtPrime`.

```lean
public theorem IsCompleteIntersection.tfae (k : Type u) [Field k] (S : Type v) [CommRing S]
    [Algebra k S] [IsLocalRing S] [Algebra.EssFiniteType k S] :
    List.TFAE
      [IsCompleteIntersection k S,
        ∀ (R : Type (max u w)) (_ : CommRing R) (_ : Algebra k R) (_ : IsRegularLocalRing R)
          (_ : Algebra.EssFiniteType k R) (f : R →ₐ[k] S),
          Function.Surjective f →
            ∃ rs : List R, RingTheory.Sequence.IsRegular R rs ∧ Ideal.ofList rs = RingHom.ker f,
        ∃ (R : Type u) (_ : CommRing R) (_ : Algebra k R) (_ : IsRegularLocalRing R) (_ :
          Algebra.EssFiniteType k R) (f : R →ₐ[k] S),
          Function.Surjective f ∧ ringKrullDim S + (RingHom.ker f).spanFinrank = ringKrullDim R,
        ∃ (A : Type u) (_ : CommRing A) (_ : Algebra k A) (_ : Algebra A S) (_ :
          IsScalarTower k A S) (a : Ideal A) (_ : a.IsPrime),
          IsGlobalCompleteIntersection k A ∧ IsLocalization.AtPrime S a,
        ∃ (A : Type u) (_ : CommRing A) (_ : Algebra k A) (_ : Algebra A S) (_ :
          IsScalarTower k A S) (a : Ideal A) (_ : a.IsPrime),
          IsLocalCompleteIntersection k A ∧ IsLocalization.AtPrime S a]
```

## Tag 00SG, a lemma

[Tag 00SG](https://stacks.math.columbia.edu/tag/00SG) in the Stacks Project.

**`IsCompleteIntersection.localization_atPrime_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/LocalRing.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/LocalRing.lean#L559). The attribute's comment: “Item (1) is `IsCompleteIntersection k Sq` for an abstract localization `Sq` of `S` at `q`, items (2) and (3) use `Localization.Away g` as Definition 00S9 does, and item (4) is a universally quantified statement over presentations `Algebra.Generators k S ι` with `ι` finite, transcribing condition (5) of Lemma 00SC — the only one of its conditions (1)-(5) that mentions neither the codimension `c` nor the conormal module, and interchangeable with the others by that lemma. See the module docstring.”. References: EGA IV (19.3.2), “special case”.

> Let `k` be a field, let `S` be a finite type `k`-algebra and let `q` be a
> prime of `S`. Then: the local ring `S_q` is a complete intersection over `k`; `S_g` is a local
> complete intersection over `k` for some `g ∉ q`; `S_g` is a global complete intersection over `k`
> for some `g ∉ q`; and, for every presentation `S = k[x_i]/I` in finitely many variables, the
> ideal `I_{q'}` of `k[x_i]_{q'}` is generated by a regular sequence — are all equivalent.

```lean
public theorem IsCompleteIntersection.localization_atPrime_tfae (k : Type u) [Field k] (S : Type v)
    [CommRing S] [Algebra k S] [Algebra.FiniteType k S] (q : Ideal S) [q.IsPrime] (Sq : Type*)
    [CommRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq q] [Algebra k Sq]
    [IsScalarTower k S Sq] :
    List.TFAE
      [IsCompleteIntersection k Sq, ∃ g ∉ q, IsLocalCompleteIntersection k (Localization.Away g),
        ∃ g ∉ q, IsGlobalCompleteIntersection k (Localization.Away g),
        ∀ (ι : Type w) [Finite ι] (P : Algebra.Generators k S ι) (A : Type (max u w)) [CommRing A]
          [Algebra P.Ring A] [IsLocalization.AtPrime A (q.comap (algebraMap P.Ring S))],
          ∃ rs : List A,
            RingTheory.Sequence.IsRegular A rs ∧
              Ideal.ofList rs = P.ker.map (algebraMap P.Ring A)]
```

## Tag 00SH, a lemma

[Tag 00SH](https://stacks.math.columbia.edu/tag/00SH) in the Stacks Project.

**`IsLocalCompleteIntersection.tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/LocalRing.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/LocalRing.lean#L703). The attribute's comment: “Item (1) is `IsLocalCompleteIntersection k S` (Definition 00S9 (2)), and items (2) and (3) say that `IsCompleteIntersection k Sq` (Definition 00SD) holds for every localization of `S` at a prime, resp. at a maximal ideal, quantified over abstract localizations `Sq` in the universe of `S` with the `k`-algebra structure induced from `S` — the hypothesis block of item (1) of Lemma 00SG. The source's finite type hypothesis is kept: items (2) and (3) do not imply it, as `ℚ(x)` over `ℚ` shows. The source's appeal to quasi-compactness of `Spec S` is absent, `IsLocalCompleteIntersection` asking for a covering by an arbitrary set of elements generating the unit ideal. See the module docstring.”.

> Let `k` be a field and let `S` be a finite type `k`-algebra. Then: `S` is a
> local complete intersection over `k`; every local ring of `S` is a complete intersection over
> `k`; and every localization of `S` at a maximal ideal is a complete intersection over `k` — are
> all equivalent. The local rings in the last two items are abstract localizations of `S`, carrying
> the `k`-algebra structure induced from `S`.

```lean
public theorem IsLocalCompleteIntersection.tfae (k : Type u) [Field k] (S : Type v) [CommRing S]
    [Algebra k S] [Algebra.FiniteType k S] :
    List.TFAE
      [IsLocalCompleteIntersection k S,
        ∀ (q : Ideal S) [q.IsPrime] (Sq : Type v) [CommRing Sq] [Algebra S Sq]
          [IsLocalization.AtPrime Sq q] [Algebra k Sq] [IsScalarTower k S Sq],
          IsCompleteIntersection k Sq,
        ∀ (m : Ideal S) [m.IsMaximal] (Sm : Type v) [CommRing Sm] [Algebra S Sm]
          [IsLocalization.AtPrime Sm m] [Algebra k Sm] [IsScalarTower k S Sm],
          IsCompleteIntersection k Sm]
```

## Tag 00SI, a lemma

[Tag 00SI](https://stacks.math.columbia.edu/tag/00SI) in the Stacks Project.

**`Algebra.IsPushout.isCompleteIntersection_localization_atPrime_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/BaseChange.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/BaseChange.lean#L360). The attribute's comment: “The base change `S' = K ⊗_k S` is an arbitrary pushout square `Algebra.IsPushout k K S S'`, the shape of the sibling 00SJ; the source's literal form satisfies it. The source's corresponding prime `q` is the contraction of `q'`, spelled `Ideal.LiesOver`, and the two local rings are abstract localizations at `q`, resp. `q'`, with the `k`-, resp. `K`-algebra structure induced from `S`, resp. `S'`, as in item (1) of Lemma 00SG. A complete intersection over a field (Definition 00SD) is `IsCompleteIntersection`. See the module docstring.”. References: EGA IV (19.3.4), “affine case”.

> Let `K/k` be a field extension, let `S` be a finite type `k`-algebra and let
> `S'` be the base change of `S` along `k → K`, so `S' = K ⊗_k S`. Let `q'` be a prime of `S'` and
> let `q` be the prime of `S` it lies over. Then the local ring `S'_{q'}` is a complete intersection
> over `K` if and only if the local ring `S_q` is a complete intersection over `k`.

```lean
public theorem Algebra.IsPushout.isCompleteIntersection_localization_atPrime_iff
    (k : Type*) [Field k] (K : Type*) [Field K] [Algebra k K]
    (S : Type*) [CommRing S] [Algebra k S] [Algebra.FiniteType k S]
    (S' : Type*) [CommRing S'] [Algebra k S'] [Algebra K S'] [Algebra S S']
    [IsScalarTower k K S'] [IsScalarTower k S S'] [Algebra.IsPushout k K S S']
    (q : Ideal S) [q.IsPrime] (q' : Ideal S') [q'.IsPrime] [q'.LiesOver q]
    (Sq : Type*) [CommRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq q]
    [Algebra k Sq] [IsScalarTower k S Sq]
    (S'q' : Type*) [CommRing S'q'] [Algebra S' S'q'] [IsLocalization.AtPrime S'q' q']
    [Algebra K S'q'] [IsScalarTower K S' S'q'] :
    IsCompleteIntersection K S'q' ↔ IsCompleteIntersection k Sq
```

## Tag 00SJ, a lemma

[Tag 00SJ](https://stacks.math.columbia.edu/tag/00SJ) in the Stacks Project.

**`Algebra.IsPushout.isLocalCompleteIntersection_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/FieldExtension.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/FieldExtension.lean#L154). The attribute's comment: “The base change `S' = S ⊗_k K` is an arbitrary pushout square `Algebra.IsPushout k K S S'`, the orientation of the sibling 00SM; the source's literal form is `inferInstance`. The source's finite type hypothesis on `S` is omitted: each side of the equivalence implies it. A local complete intersection over a field (Definition 00S9 (2)) is `IsLocalCompleteIntersection`. See the module docstring.”.

> Let `k → K` be a field extension, let `S` be a `k`-algebra and let `S'` be
> the base change of `S` along `k → K`, so `S' = S ⊗_k K`. Then `S'` is a local complete
> intersection over `K` if and only if `S` is a local complete intersection over `k`.

```lean
public theorem Algebra.IsPushout.isLocalCompleteIntersection_iff (k K S S' : Type*) [Field k]
    [Field K] [CommRing S] [CommRing S'] [Algebra k K] [Algebra k S] [Algebra k S'] [Algebra K S']
    [Algebra S S'] [IsScalarTower k K S'] [IsScalarTower k S S'] [Algebra.IsPushout k K S S'] :
    IsLocalCompleteIntersection K S' ↔ IsLocalCompleteIntersection k S
```

## Tag 02JP, a lemma

[Tag 02JP](https://stacks.math.columbia.edu/tag/02JP) in the Stacks Project.

**`exists_isRegular_ofList_eq_ker_algebraMap_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Local.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Local.lean#L616). The attribute's comment: “The square is `IsScalarTower R A B` and `IsScalarTower R S B` with `R → A` and `S → B` surjective, `I` and `J` being their kernels, and `J̄` is the image of `J` in `S ⧸ 𝔪_R S`. Stated more generally than the source: `R` is only assumed Cohen-Macaulay (regular local rings are, by 00NQ), and `S̄` is not assumed regular, which the argument does not use. `S` is assumed Noetherian, as the source's appeals to 00MG and 00ME require. See the module docstring.”.

> **Descent of regular sequences along a flat square of local rings.** Let
> ```
> B ← S
> ↑   ↑
> A ← R
> ```
> be a commutative square of rings in which `R` is a Cohen–Macaulay Noetherian local ring, `S` is
> a Noetherian local ring, `A = R/I` and `B = S/J` are quotients, and `R → S` and `A → B` are flat.
> If `J` is generated by a regular sequence, and the image `J̄` of `J` in `S̄ = S/𝔪_R S` is
> generated by a regular sequence, then `I` is generated by a regular sequence.
>
> The quotients are encoded by the surjectivity of `R → A` and `S → B`, the ideals `I` and `J`
> being their kernels. See the module docstring.

```lean
theorem exists_isRegular_ofList_eq_ker_algebraMap_of_flat
    {R S A B : Type*} [CommRing R] [CommRing S] [CommRing A] [CommRing B]
    [Algebra R S] [Algebra R A] [Algebra A B] [Algebra S B] [Algebra R B]
    [IsScalarTower R A B] [IsScalarTower R S B]
    [IsLocalRing R] [IsNoetherianRing R] [IsLocalRing S] [IsNoetherianRing S]
    [Module.Flat R S] [Module.Flat A B]
    (hR : Module.IsMaximalCohenMacaulay R R)
    (hA : Function.Surjective (algebraMap R A)) (hB : Function.Surjective (algebraMap S B))
    (hJ : ∃ rs : List S, IsRegular S rs ∧ Ideal.ofList rs = RingHom.ker (algebraMap S B))
    (hJbar : ∃ rs : List (S ⧸ (maximalIdeal R).map (algebraMap R S)),
      IsRegular (S ⧸ (maximalIdeal R).map (algebraMap R S)) rs ∧
        Ideal.ofList rs = (RingHom.ker (algebraMap S B)).map (Ideal.Quotient.mk _)) :
    ∃ rs : List R, IsRegular R rs ∧ Ideal.ofList rs = RingHom.ker (algebraMap R A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.135, Tag 00S8](https://stacks.math.columbia.edu/tag/00S8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
