---
declaration: section
origin: cited
lean: Stacks.TraceFormula.AbstractTraceFormula, Stacks.TraceFormula.HasAbstractTraceFormula, Stacks.TraceFormula.frobenius_conj, Stacks.TraceFormula.isTopologicalGroup_gamma, Stacks.TraceFormula.eq_intCast_traceParameter, Stacks.TraceFormula.abs_traceParameter_lt, Stacks.TraceFormula.exists_intCast_eq_and_abs_lt, Stacks.TraceFormula.commutativeExample_hasAbstractTraceFormula_one
statement: formalized
proof: formalized
---

# 64.30 Abstract trace formula

Section 64.30 of the Stacks Project, [Tag 03VO](https://stacks.math.columbia.edu/tag/03VO). 2 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03VO, the section

[Tag 03VO](https://stacks.math.columbia.edu/tag/03VO) in the Stacks Project.

**`Stacks.TraceFormula.AbstractTraceFormula`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/AbstractTraceFormula.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/AbstractTraceFormula.lean#L121). The attribute's comment: “an extension 1 → G → Γ → Ẑ → 1 of profinite groups has an abstract trace formula”.

> **Stacks Project, Section 03VO.** An *abstract trace formula* for an extension of profinite
> groups `1 → G → Γ → Ẑ → 1`, given by a continuous surjective degree map `deg : Γ → Ẑ` with kernel
> `G`: an integer `q ≥ 1`, for every `d` a finite set `S_d` and for each `x ∈ S_d` a conjugacy class
> `F_x` of degree `d` (for `d ≥ 1`), such that `cd_ℓ(G) < ∞` for all primes `ℓ ∤ q` and such that
> for all finite rings `Λ` with `q ∈ Λ^*`, all finite projective `Λ`-modules `M` with continuous
> `Γ`-action and all `n > 0`, the derived homology `LH₀(G, M) = M ⊗^L_{Λ[[G]]} Λ` is perfect and
> `∑_{d ∣ n} d ∑_{x ∈ S_d} Tr(F_x^{n/d} | M) = q^n Tr(F^n | LH₀(G, M))` in `Λ^♮`, for every element
> `F` of degree one and all representatives of the classes `F_x`.

```lean
public structure AbstractTraceFormula (Γ : Type u) [Group Γ] [TopologicalSpace Γ]
    [IsTopologicalGroup Γ] [CompactSpace Γ] [TotallyDisconnectedSpace Γ]
    (deg : Γ →* Multiplicative ProfiniteIntegers) (hdeg : Continuous deg)
    (hsurj : Function.Surjective deg)
```

**`Stacks.TraceFormula.HasAbstractTraceFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/AbstractTraceFormula.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/AbstractTraceFormula.lean#L164). The attribute's comment: “has an abstract trace formula”.

> **Stacks Project, Section 03VO.** The extension `1 → G → Γ → Ẑ → 1` *has an abstract trace
> formula* if the data of `Stacks.TraceFormula.AbstractTraceFormula` exist.

```lean
public def HasAbstractTraceFormula (Γ : Type u) [Group Γ] [TopologicalSpace Γ]
    [IsTopologicalGroup Γ] [CompactSpace Γ] [TotallyDisconnectedSpace Γ]
    (deg : Γ →* Multiplicative ProfiniteIntegers) (hdeg : Continuous deg)
    (hsurj : Function.Surjective deg) : Prop
```

## Tag 03VQ, an example

[Tag 03VQ](https://stacks.math.columbia.edu/tag/03VQ) in the Stacks Project.

**`Stacks.TraceFormula.frobenius_conj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean#L189). The attribute's comment: “the exact sequence 1 → Ẑ^\{(q)} → Γ → Ẑ → 1 with F of degree 1 and F x F⁻¹ = u x, as an extension of groups”.

> **Stacks Project, Tag 03VQ.** The extension `1 → Ẑ^{(q)} → Γ → Ẑ → 1` exhibited by the
> semidirect product: conjugation by the Frobenius element is multiplication by the unit
> `u = χ 1`, that is, `F x F⁻¹ = u x` for every `x` in the kernel `G = Ẑ^{(q)}`.

```lean
public theorem frobenius_conj (x : RestrictedProfiniteIntegers q) :
    frobenius χ * incl χ (Multiplicative.ofAdd x) * (frobenius χ)⁻¹ =
      incl χ (Multiplicative.ofAdd
        ((χ (Multiplicative.ofAdd (1 : ProfiniteIntegers)) :
          RestrictedProfiniteIntegers q) * x))
```

**`Stacks.TraceFormula.isTopologicalGroup_gamma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean#L228). The attribute's comment: “Γ is a profinite group”.

> **Stacks Project, Tag 03VQ.** The extension `Γ = Ẑ^{(q)} ⋊ Ẑ` is a topological group, as
> soon as the powers `u^z = χ z` of the unit vary continuously with `z`. Together with
> `Stacks.TraceFormula.compactSpace_gamma` and
> `Stacks.TraceFormula.totallyDisconnectedSpace_gamma` this makes `Γ` profinite.

```lean
public theorem isTopologicalGroup_gamma (hχ : Continuous χ) : IsTopologicalGroup (Gamma χ)
```

**`Stacks.TraceFormula.eq_intCast_traceParameter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean#L313). The attribute's comment: “qu = a ∈ ℤ, with a = q - #S₁”.

> **Stacks Project, Tag 03VQ.** The congruence for the trivial coefficient modules forces
> `qu` to be the ordinary integer `a = q - #S_1`.

```lean
public theorem eq_intCast_traceParameter (h : IsTrivialModuleCongruence q b s) :
    b = ((traceParameter q s : ℤ) : RestrictedProfiniteIntegers q)
```

**`Stacks.TraceFormula.abs_traceParameter_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean#L356). The attribute's comment: “the bound |a| < q”.

> **Stacks Project, Tag 03VQ.** If some `S_d` is nonempty then the integer `a` with `qu = a`
> satisfies `|a| < q`.

```lean
public theorem abs_traceParameter_lt (hq : 1 ≤ q) (h : IsTrivialModuleCongruence q b s)
    (hs : ∃ d : ℕ, 0 < d ∧ s d ≠ 0) : |traceParameter q s| < (q : ℤ)
```

**`Stacks.TraceFormula.exists_intCast_eq_and_abs_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExample.lean#L367). The attribute's comment: “q^n - (qu)^n ≡ ∑\_\{d ∣ n} d #S\_d for all moduli prime to q implies qu = a ∈ ℤ with |a| < q”.

> **Stacks Project, Tag 03VQ.** For a unit `u` of `Ẑ^{(q)}`, the congruence
> `q^n - (qu)^n ≡ ∑_{d ∣ n} d · #S_d` for the trivial coefficient modules forces `qu` to be an
> integer `a` with `|a| < q`, provided some `S_d` is nonempty.

```lean
public theorem exists_intCast_eq_and_abs_lt (hq : 1 ≤ q) (u : (RestrictedProfiniteIntegers q)ˣ)
    (s : ℕ → ℕ)
    (h : IsTrivialModuleCongruence q ((q : RestrictedProfiniteIntegers q) * u) s)
    (hs : ∃ d : ℕ, 0 < d ∧ s d ≠ 0) :
    ∃ a : ℤ, (q : RestrictedProfiniteIntegers q) * u =
      (a : RestrictedProfiniteIntegers q) ∧ |a| < (q : ℤ)
```

**`Stacks.TraceFormula.commutativeExample_hasAbstractTraceFormula_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleExistence.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleExistence.lean#L261). The attribute's comment: “the case u = 1: Γ = Ẑ^(q) × Ẑ has an abstract trace formula with integer q and all S\_d empty, so qu = a = q and the source's bound |a| < q fails”.

> **Stacks Project, Tag 03VQ: the case `u = 1`, a counterexample to `|a| < q`.** For every
> `q ≥ 1` the extension `1 → Ẑ^{(q)} → Γ → Ẑ → 1` with `F x F⁻¹ = x` (that is, `u = 1`,
> `Γ = Ẑ^{(q)} × Ẑ`) has an abstract trace formula with integer `q` and all the sets `S_d` empty;
> for it `qu = a = q`, so `|a| < q` fails, and the corrected integrality statement
> `Stacks.TraceFormula.commutativeExample_integrality` (`|a| ≤ q`, with `|a| < q` exactly when
> `u ≠ 1`) is sharp.

```lean
public theorem commutativeExample_hasAbstractTraceFormula_one (hq : 1 ≤ q) :
    ∃ T : AbstractTraceFormula (Gamma (trivialCharacter (q := q))) (degree _)
        (continuous_degree _) (degree_surjective _),
      T.q = q ∧ (∀ d, IsEmpty (T.S d)) ∧
        frobenius (trivialCharacter (q := q)) * incl _ (Multiplicative.ofAdd 1) *
            (frobenius (trivialCharacter (q := q)))⁻¹ = incl _ (Multiplicative.ofAdd 1) ∧
        ¬ |((q : ℤ) * 1)| < q
```

**`Stacks.TraceFormula.commutativeExample_congruence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleIntegrality.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleIntegrality.lean#L66). The attribute's comment: “q^n - (qu)^n ≡ ∑\_\{d ∣ n} d #S\_d in ℤ/m for all m prime to q, derived from the abstract trace formula on the trivial modules ℤ/m”.

> **Stacks Project, Tag 03VQ: the congruence.** If the extension
> `1 → Ẑ^{(q)} → Γ → Ẑ → 1` with `F x F⁻¹ = u x` has an abstract trace formula with integer `q`,
> then `q^n - (qu)^n ≡ ∑_{d ∣ n} d #S_d` in `ℤ/m` for every `m` prime to `q`: as an identity in
> `Ẑ^{(q)} = lim_{(m,q)=1} ℤ/m`, and, `qu` being the integer `a = q - #S_1`, as the identity
> `q^n - a^n = ∑_{d ∣ n} d #S_d` of integers.

```lean
public theorem commutativeExample_congruence (n : ℕ) (hn : 0 < n) :
    (q : RestrictedProfiniteIntegers q) ^ n - ((q : RestrictedProfiniteIntegers q) * u) ^ n =
        (pointCountSum (fun d => Fintype.card (T.S d)) n : RestrictedProfiniteIntegers q) ∧
      (q : ℤ) ^ n - ((q : ℤ) - Fintype.card (T.S 1)) ^ n =
        pointCountSum (fun d => Fintype.card (T.S d)) n
```

**`Stacks.TraceFormula.commutativeExample_integrality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleIntegrality.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleIntegrality.lean#L88). The attribute's comment: “corrected: qu = a ∈ ℤ with |a| ≤ q, and |a| < q iff u ≠ 1 iff some S\_d is nonempty; the source's unconditional |a| < q fails for u = 1, where Γ = Ẑ^(q) × Ẑ has an abstract trace formula with all S\_d empty”.

> **Stacks Project, Tag 03VQ (corrected).** If the extension `1 → Ẑ^{(q)} → Γ → Ẑ → 1` with
> `F x F⁻¹ = u x` has an abstract trace formula with integer `q` and sets `S_d`, then `qu = a ∈ ℤ`
> with `a = q - #S_1`, and `|a| ≤ q`; moreover `|a| < q` exactly when `u ≠ 1`, exactly when some
> `S_d` (`d ≥ 1`) is nonempty. The source's unconditional `|a| < q` fails for `u = 1`.

```lean
public theorem commutativeExample_integrality :
    ∃ a : ℤ, (q : RestrictedProfiniteIntegers q) * u = (a : RestrictedProfiniteIntegers q) ∧
      a = q - Fintype.card (T.S 1) ∧ |a| ≤ q ∧
      (|a| < q ↔ u ≠ 1) ∧ (|a| < q ↔ ∃ d : ℕ, 0 < d ∧ Nonempty (T.S d))
```

**`Stacks.TraceFormula.commutativeExample_card_eq_of_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleIntegrality.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleIntegrality.lean#L120). The attribute's comment: “the special case a = 1: #S₁ = q - 1 and #S₂ = ((q² - 1) - (q - 1))/2”.

> **Stacks Project, Tag 03VQ: the special case `a = 1`.** If `qu = 1`, the sets `S_1` and
> `S_2` have `q - 1` and `((q² - 1) - (q - 1))/2` elements, the numbers of closed points of
> `G_{m, F_q}` of degree `1` and `2`.

```lean
public theorem commutativeExample_card_eq_of_eq_one
    (h1 : (q : RestrictedProfiniteIntegers q) * u = 1) :
    Fintype.card (T.S 1) = q - 1 ∧ Fintype.card (T.S 2) = ((q ^ 2 - 1) - (q - 1)) / 2
```

**`Stacks.TraceFormula.commutativeExample_hasAbstractTraceFormula_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleInverse.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/CommutativeExampleInverse.lean#L610). The attribute's comment: “the special case a = 1 does occur: Γ = Ẑ^(q) ⋊ Ẑ with F x F⁻¹ = q⁻¹ x has an abstract trace formula with integer q, with #S₁ = q - 1 and #S₂ = ((q² - 1) - (q - 1))/2”.

> **Stacks Project, Tag 03VQ: the special case `a = 1` occurs.** For every `q ≥ 2` the
> extension `1 → Ẑ^{(q)} → Γ → Ẑ → 1` with `F x F⁻¹ = q⁻¹ x` (so `u = q⁻¹` and `qu = a = 1`) has an
> abstract trace formula with integer `q`; its sets `S_d` are the orbits of exact size `d` of
> multiplication by `q` on `ℤ/(q^d - 1)`, and `#S_1 = q - 1`, `#S_2 = ((q² - 1) - (q - 1))/2`.

```lean
public theorem commutativeExample_hasAbstractTraceFormula_inverse :
    ∃ T : AbstractTraceFormula (Gamma (inverseCharacter q)) (degree _) (continuous_degree _)
        (degree_surjective _),
      T.q = q ∧
        (∀ x : RestrictedProfiniteIntegers q,
          frobenius (inverseCharacter q) * incl _ (Multiplicative.ofAdd x) *
              (frobenius (inverseCharacter q))⁻¹ =
            incl _ (Multiplicative.ofAdd ((qInv q : RestrictedProfiniteIntegers q) * x))) ∧
        (q : RestrictedProfiniteIntegers q) * (qInv q : RestrictedProfiniteIntegers q) = 1 ∧
        (∀ d, T.S d = Necklace.Orbits q d) ∧
        Fintype.card (T.S 1) = q - 1 ∧ Fintype.card (T.S 2) = ((q ^ 2 - 1) - (q - 1)) / 2
```

**`AlgebraicGeometry.TameMultiplicativeGroup.tameFundamentalGroup_zmod_hasAbstractTraceFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/TameMultiplicativeGroupExample.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/TameMultiplicativeGroupExample.lean#L89). The attribute's comment: “the special case a = 1 does occur with Γ = π₁ᵗ(𝐆\_\{m,𝔽\_p}, η̄), #S₁ = q - 1 and #S₂ = ((q² - 1) - (q - 1))/2”.

> **Stacks Project, Tag 03VQ: the special case `a = 1` occurs with
> `Γ = π₁ᵗ(𝐆_{m,𝔽_p}, η̄)`, `#S_1 = q - 1` and `#S_2 = ((q² - 1) - (q - 1))/2`.** For `p` prime there
> is an isomorphism of topological groups `e : Ẑ^{(p)} ⋊ Ẑ ≃ₜ* π₁ᵗ(𝐆_{m,𝔽_p}, η̄)`, with
> `F x F⁻¹ = u x`, `u = p⁻¹`, compatible with the degrees (an element of degree `d` acts on the
> constants `𝔽_{p^n}` of the points of every tame cover as the geometric Frobenius to the power
> `d mod n`, so the kernel `Ẑ^{(p)}` is the geometric part); and this extension has an abstract trace
> formula with integer `q = p`, `qu = a = 1`, `#S_1 = q - 1` and `#S_2 = ((q² - 1) - (q - 1))/2`.

```lean
theorem tameFundamentalGroup_zmod_hasAbstractTraceFormula (p : ℕ) [Fact p.Prime] :
    ∃ e : Gamma (inverseCharacter p) ≃ₜ* tameFundamentalGroup (ZMod p),
      (∀ (γ : Gamma (inverseCharacter p)) (Y : TameCover (ZMod p))
        (y : (tameFiberFunctor (ZMod p)).obj Y) (c : Γ(Y.obj.left, ⊤)) (n : ℕ) (hn : n ≠ 0),
          fiberRingHom y c ∈ frobField (ZMod p) n →
          fiberRingHom (autApply (e γ) Y y) c ^ (p ^ (restrictedMod 1 n hn
            (Nat.coprime_one_right n) (Multiplicative.toAdd (degree _ γ))).val) =
            fiberRingHom y c) ∧
      ∃ T : AbstractTraceFormula (Gamma (inverseCharacter p)) (degree _) (continuous_degree _)
          (degree_surjective _),
        T.q = p ∧
          (∀ x : RestrictedProfiniteIntegers p,
            frobenius (inverseCharacter p) * incl _ (Multiplicative.ofAdd x) *
                (frobenius (inverseCharacter p))⁻¹ =
              incl _ (Multiplicative.ofAdd ((qInv p : RestrictedProfiniteIntegers p) * x))) ∧
          (p : RestrictedProfiniteIntegers p) * (qInv p : RestrictedProfiniteIntegers p) = 1 ∧
          (∀ d, T.S d = Necklace.Orbits p d) ∧
          Fintype.card (T.S 1) = p - 1 ∧ Fintype.card (T.S 2) = ((p ^ 2 - 1) - (p - 1)) / 2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.30, Tag 03VO](https://stacks.math.columbia.edu/tag/03VO)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
