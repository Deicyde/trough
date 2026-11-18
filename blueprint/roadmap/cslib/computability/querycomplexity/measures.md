---
catalog: module
lean: Cslib.BitString.IsSensitiveCoord, Cslib.BitString.sensitiveCoords, Cslib.BitString.mem_sensitiveCoords, Cslib.BitString.sensitivityAt, Cslib.BitString.sensitivity, Cslib.BitString.card_le_sensitivityAt, Cslib.BitString.sensitivityAt_le_sensitivity, Cslib.BitString.card_le_sensitivity_of_forall_isSensitiveCoord, Cslib.BitString.sensitivityAt_le_card, Cslib.BitString.sensitivity_le_card, Cslib.QueryComplexity.IsSensitiveBlock, Cslib.QueryComplexity.IsSensitiveFamily, Cslib.QueryComplexity.sensitiveFamilies, Cslib.QueryComplexity.mem_sensitiveFamilies, Cslib.QueryComplexity.blockSensitivityAt, Cslib.QueryComplexity.blockSensitivity, Cslib.QueryComplexity.card_le_blockSensitivityAt, Cslib.QueryComplexity.blockSensitivityAt_le_blockSensitivity, Cslib.QueryComplexity.card_le_blockSensitivity, Cslib.QueryComplexity.isSensitiveBlock_singleton, Cslib.QueryComplexity.singletonFamily, Cslib.QueryComplexity.mem_singletonFamily, Cslib.QueryComplexity.card_singletonFamily, Cslib.QueryComplexity.isSensitiveFamily_singletonFamily, Cslib.QueryComplexity.sensitivityAt_le_blockSensitivityAt, Cslib.QueryComplexity.sensitivity_le_blockSensitivity, Cslib.QueryComplexity.IsMinimalSensitiveBlock, Cslib.QueryComplexity.IsMinimalSensitiveBlock.not_isSensitiveBlock_erase, Cslib.QueryComplexity.IsMinimalSensitiveBlock.isSensitiveCoord_flipBlock, Cslib.QueryComplexity.IsMinimalSensitiveBlock.card_le_sensitivity, Cslib.QueryComplexity.IsCertificate, Cslib.QueryComplexity.Forces, Cslib.QueryComplexity.isCertificate_iff_forces_restrict, Cslib.QueryComplexity.forces_iff_isCertificate_support, Cslib.QueryComplexity.isCertificate_univ, Cslib.QueryComplexity.filter_isCertificate_nonempty, Cslib.QueryComplexity.certificateComplexityAt, Cslib.QueryComplexity.certificateComplexityAt_le, Cslib.QueryComplexity.le_certificateComplexityAt, Cslib.QueryComplexity.exists_isCertificate_card_eq, Cslib.QueryComplexity.forcingAssignments, Cslib.QueryComplexity.mem_forcingAssignments, Cslib.QueryComplexity.ofBitString_mem_forcingAssignments, Cslib.QueryComplexity.forcingAssignments_nonempty, Cslib.QueryComplexity.certificateComplexityAt_eq_inf'_size, Cslib.QueryComplexity.certificateComplexity, Cslib.QueryComplexity.certificateComplexityAt_le_certificateComplexity, Cslib.QueryComplexity.certificateComplexityAt_le_card, Cslib.QueryComplexity.certificateComplexity_le_card, Cslib.QueryComplexity.sensitiveBlock_inter_nonempty, Cslib.QueryComplexity.card_le_card_of_isSensitiveFamily, Cslib.QueryComplexity.blockSensitivityAt_le_certificateComplexityAt, Cslib.QueryComplexity.blockSensitivity_le_certificateComplexity, Cslib.QueryComplexity.blockSensitivityAt_le_card, Cslib.QueryComplexity.blockSensitivity_le_card
statement: formalized
proof: formalized
---

# Boolean function complexity measures

`Cslib.Computability.QueryComplexity.Measures`, in [Cslib/Computability/QueryComplexity/Measures.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean), by Vignesh Karri.

> Sensitivity `s(f)`, block sensitivity `bs(f)` and certificate complexity `C(f)`, together with
> the chain `s(f) ≤ bs(f) ≤ C(f)`. Notation follows [AroraBarak09]; the pointwise measures
> `s(f, x)`, `bs(f, x)`, `C(f, x)` are those of [Jukna, Section 14.3][Jukna2012].
>
> ## Main definitions
>
> - `BitString.sensitivity`: `s(f)`, the maximum over inputs of the number of sensitive coordinates.
> - `blockSensitivity`: `bs(f)`, the maximum over inputs of the maximum number of disjoint sensitive
>   blocks.
> - `IsCertificate`: a set of coordinates whose values at `x` pin down `f x`, as in
>   [Jukna, Section 14.3][Jukna2012].
> - `Forces`: a partial assignment forces the value `b`, as in [BuhrmanDeWolf2002]. At a fixed input
>   an assignment consistent with `x` is determined by its support, so the pointwise measure needs no
>   bit values.
> - `certificateComplexity`: `C(f)`, the maximum over inputs of the smallest certificate size.
>
> ## Main results
>
> - `sensitivity_le_blockSensitivity`: `s(f) ≤ bs(f)`.
> - `blockSensitivity_le_certificateComplexity`: `bs(f) ≤ C(f)`.
> - `isCertificate_iff_forces_restrict`, `forces_iff_isCertificate_support`: `IsCertificate` and
>   `Forces` agree at a fixed input.
> - `certificateComplexityAt_eq_inf'_size`: `C(f, x)` is the minimum size of a forcing assignment
>   consistent with `x`.
> - `|B| ≤ s(f)` for a minimal sensitive block `B`.
>
> ## References
>
> * [S. Arora, B. Barak, *Computational Complexity: A Modern Approach*][AroraBarak09],
>   Section 12.2 (Certificate Complexity) and Section 12.5.1 (Sensitivity).
> * [H. Buhrman, R. de Wolf, *Complexity measures and decision tree complexity:
>   a survey*][BuhrmanDeWolf2002]
> * [S. Jukna, *Boolean Function Complexity: Advances and Frontiers*][Jukna2012], Section 14.3.

> ## Sensitivity

`Cslib.BitString.IsSensitiveCoord` (definition, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L65))

> Coordinate `i` is sensitive for `f` at `x` when flipping it flips `f`.

```lean
def IsSensitiveCoord (f : BooleanFunction n) (x : BitString n) (i : Fin n) : Prop
```

`Cslib.BitString.sensitiveCoords` (definition, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L72))

> The set of coordinates sensitive for `f` at `x`.

```lean
def sensitiveCoords (f : BooleanFunction n) (x : BitString n) : Finset (Fin n)
```

`Cslib.BitString.mem_sensitiveCoords` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L77))

> The bridge between the predicate and the `Finset` it cuts out.

```lean
lemma mem_sensitiveCoords {f : BooleanFunction n} {x : BitString n} {i : Fin n} :
    i ∈ sensitiveCoords f x ↔ IsSensitiveCoord f x i
```

`Cslib.BitString.sensitivityAt` (definition, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L82))

> The number of sensitive coordinates in input `x`, usually denoted `s(f, x)`.

```lean
def sensitivityAt (f : BooleanFunction n) (x : BitString n) : ℕ
```

`Cslib.BitString.sensitivity` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L85))

> The maximum sensitivity over all inputs, denoted `s(f)`.

```lean
def sensitivity (f : BooleanFunction n) : ℕ
```

`Cslib.BitString.card_le_sensitivityAt` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L88))

> Lower-bound rule for `s(f, x)`: exhibit a set of sensitive coordinates.

```lean
lemma card_le_sensitivityAt {f : BooleanFunction n} {x : BitString n} {S : Finset (Fin n)}
    (h : ∀ i ∈ S, IsSensitiveCoord f x i) : S.card ≤ sensitivityAt f x
```

`Cslib.BitString.sensitivityAt_le_sensitivity` (lemma, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L94))

> The sensitivity at a single input is at most the sensitivity of `f`: `s(f, x) ≤ s(f)`.

```lean
lemma sensitivityAt_le_sensitivity (f : BooleanFunction n) (x : BitString n) :
    sensitivityAt f x ≤ sensitivity f
```

`Cslib.BitString.card_le_sensitivity_of_forall_isSensitiveCoord` (lemma, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L99))

> Lower-bound rule for `s(f)`: sensitive coordinates at any input suffice.

```lean
lemma card_le_sensitivity_of_forall_isSensitiveCoord {f : BooleanFunction n} {x : BitString n}
    {S : Finset (Fin n)} (h : ∀ i ∈ S, IsSensitiveCoord f x i) : S.card ≤ sensitivity f
```

`Cslib.BitString.sensitivityAt_le_card` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L104))

> `s(f, x) ≤ n`: there are only `n` coordinates.

```lean
theorem sensitivityAt_le_card (f : BooleanFunction n) (x : BitString n) : sensitivityAt f x ≤ n
```

`Cslib.BitString.sensitivity_le_card` (theorem, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L108))

> `s(f) ≤ n`.

```lean
theorem sensitivity_le_card (f : BooleanFunction n) : sensitivity f ≤ n
```

> ## Block sensitivity

`Cslib.QueryComplexity.IsSensitiveBlock` (definition, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L120))

> Block `B` is sensitive for `f` at `x` when flipping all bits of `B` flips `f`.

```lean
def IsSensitiveBlock (f : BooleanFunction n) (x : BitString n) (B : Block n) : Prop
```

`Cslib.QueryComplexity.IsSensitiveFamily` (definition, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L128))

> Every member flips `f`, and the members are pairwise disjoint.

```lean
def IsSensitiveFamily (f : BooleanFunction n) (x : BitString n) (F : Finset (Block n)) : Prop
```

`Cslib.QueryComplexity.sensitiveFamilies` (definition, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L137))

> All sensitive families.

```lean
def sensitiveFamilies (f : BooleanFunction n) (x : BitString n) : Finset (Finset (Block n))
```

`Cslib.QueryComplexity.mem_sensitiveFamilies` (lemma, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L141))

```lean
lemma mem_sensitiveFamilies {f : BooleanFunction n} {x : BitString n} {F : Finset (Block n)} :
    F ∈ sensitiveFamilies f x ↔ IsSensitiveFamily f x F
```

`Cslib.QueryComplexity.blockSensitivityAt` (definition, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L148))

> The block sensitivity of `f` at `x`: the largest number of pairwise disjoint blocks of
> coordinates such that flipping every coordinate of any one block flips `f`. Usually denoted
> `bs(f, x)`.

```lean
def blockSensitivityAt (f : BooleanFunction n) (x : BitString n) : ℕ
```

`Cslib.QueryComplexity.blockSensitivity` (definition, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L152))

> The maximum block sensitivity over all inputs, denoted `bs(f)`.

```lean
def blockSensitivity (f : BooleanFunction n) : ℕ
```

`Cslib.QueryComplexity.card_le_blockSensitivityAt` (lemma, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L155))

> Lower-bound rule for `bs(f, x)`: exhibit one sensitive family.

```lean
lemma card_le_blockSensitivityAt {f : BooleanFunction n} {x : BitString n} {F : Finset (Block n)}
    (h : IsSensitiveFamily f x F) : F.card ≤ blockSensitivityAt f x
```

`Cslib.QueryComplexity.blockSensitivityAt_le_blockSensitivity` (lemma, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L160))

> The block sensitivity at a single input is at most that of `f`: `bs(f, x) ≤ bs(f)`.

```lean
lemma blockSensitivityAt_le_blockSensitivity (f : BooleanFunction n) (x : BitString n) :
    blockSensitivityAt f x ≤ blockSensitivity f
```

`Cslib.QueryComplexity.card_le_blockSensitivity` (lemma, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L165))

> Lower-bound rule for `bs(f)`.

```lean
lemma card_le_blockSensitivity {f : BooleanFunction n} {x : BitString n} {F : Finset (Block n)}
    (h : IsSensitiveFamily f x F) : F.card ≤ blockSensitivity f
```

> ## Sensitive singletons

`Cslib.QueryComplexity.isSensitiveBlock_singleton` (lemma, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L173))

> A singleton block is sensitive if and only if its coordinate is.

```lean
lemma isSensitiveBlock_singleton {f : BooleanFunction n} {x : BitString n} {i : Fin n} :
    IsSensitiveBlock f x {i} ↔ IsSensitiveCoord f x i
```

> ## `s(f) ≤ bs(f)`

`Cslib.QueryComplexity.singletonFamily` (definition, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L180))

> One block per sensitive coordinate.

```lean
def singletonFamily (f : BooleanFunction n) (x : BitString n) : Finset (Block n)
```

`Cslib.QueryComplexity.mem_singletonFamily` (lemma, [line 185](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L185))

> Membership in the singleton family: one block per sensitive coordinate.

```lean
lemma mem_singletonFamily {f : BooleanFunction n} {x : BitString n} {B : Block n} :
    B ∈ singletonFamily f x ↔ ∃ i, IsSensitiveCoord f x i ∧ {i} = B
```

`Cslib.QueryComplexity.card_singletonFamily` (lemma, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L191))

> The singleton family has one block per sensitive coordinate, so `s(f, x)` of them.

```lean
lemma card_singletonFamily {f : BooleanFunction n} {x : BitString n} :
    (singletonFamily f x).card = sensitivityAt f x
```

`Cslib.QueryComplexity.isSensitiveFamily_singletonFamily` (lemma, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L197))

> Singletons of distinct sensitive coordinates do form a sensitive family: each
> flips `f`, and distinct singletons are disjoint.

```lean
lemma isSensitiveFamily_singletonFamily {f : BooleanFunction n} {x : BitString n} :
    IsSensitiveFamily f x (singletonFamily f x)
```

`Cslib.QueryComplexity.sensitivityAt_le_blockSensitivityAt` (theorem, [line 209](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L209))

> Pointwise: `s(f, x) ≤ bs(f, x)`.

```lean
theorem sensitivityAt_le_blockSensitivityAt (f : BooleanFunction n) (x : BitString n) :
    sensitivityAt f x ≤ blockSensitivityAt f x
```

`Cslib.QueryComplexity.sensitivity_le_blockSensitivity` (theorem, [line 214](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L214))

> Every sensitive coordinate is a sensitive block of size one, so `s(f) ≤ bs(f)`.

```lean
theorem sensitivity_le_blockSensitivity (f : BooleanFunction n) :
    sensitivity f ≤ blockSensitivity f
```

> ## Minimal sensitive blocks

`Cslib.QueryComplexity.IsMinimalSensitiveBlock` (definition, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L221))

> `B` is sensitive, and no proper subset of `B` is sensitive.

```lean
def IsMinimalSensitiveBlock (f : BooleanFunction n) (x : BitString n) (B : Block n) : Prop
```

`Cslib.QueryComplexity.IsMinimalSensitiveBlock.not_isSensitiveBlock_erase` (lemma, [line 233](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L233))

> Dropping any coordinate from a minimal sensitive block breaks sensitivity.

```lean
lemma not_isSensitiveBlock_erase (hB : IsMinimalSensitiveBlock f x B) (hi : i ∈ B) :
    ¬ IsSensitiveBlock f x (B.erase i)
```

`Cslib.QueryComplexity.IsMinimalSensitiveBlock.isSensitiveCoord_flipBlock` (lemma, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L239))

> Every coordinate of a minimal sensitive block is sensitive at the input which
> has the minimal sensitive block flipped.

```lean
lemma isSensitiveCoord_flipBlock (hB : IsMinimalSensitiveBlock f x B) (hi : i ∈ B) :
    IsSensitiveCoord f (flipBlock B x) i
```

`Cslib.QueryComplexity.IsMinimalSensitiveBlock.card_le_sensitivity` (theorem, [line 247](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L247))

> `|B| ≤ s(f)` for a minimal sensitive block `B`.

```lean
theorem card_le_sensitivity (hB : IsMinimalSensitiveBlock f x B) : B.card ≤ sensitivity f
```

> ## Certificates
>
> A certificate for `x` is a set of coordinates whose values at `x` already determine `f x`
> [Jukna, Section 14.3][Jukna2012]. The survey [BuhrmanDeWolf2002] instead works with partial
> assignments that force a value; `Forces` keeps that in general form, with the forced value `b` a
> parameter, and the two views agree at a fixed input.

`Cslib.QueryComplexity.IsCertificate` (definition, [line 262](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L262))

> `S` is a certificate for `f` at `x`: every input agreeing with `x` on `S` takes the same
> value, so `f x` can be read off from the bits of `x` in `S`.

```lean
def IsCertificate (f : BooleanFunction n) (x : BitString n) (S : Finset (Fin n)) : Prop
```

`Cslib.QueryComplexity.Forces` (definition, [line 270](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L270))

> `C` forces the value `b`: everything consistent with `C` has `f = b`.

```lean
def Forces (f : BooleanFunction n) (C : PartialAssignment n) (b : Bool) : Prop
```

`Cslib.QueryComplexity.isCertificate_iff_forces_restrict` (theorem, [line 278](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L278))

> `S` is a certificate for `x` if and only if `x` restricted to `S` forces `f x`.

```lean
theorem isCertificate_iff_forces_restrict {f : BooleanFunction n} {x : BitString n}
    {S : Finset (Fin n)} : IsCertificate f x S ↔ Forces f (restrict x S) (f x)
```

`Cslib.QueryComplexity.forces_iff_isCertificate_support` (theorem, [line 284](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L284))

> A partial assignment consistent with `x` forces `f x` if and only if its support is a
> certificate for `x`.

```lean
theorem forces_iff_isCertificate_support {f : BooleanFunction n} {x : BitString n}
    {C : PartialAssignment n} (hC : Agrees C x) :
    Forces f C (f x) ↔ IsCertificate f x (support C)
```

`Cslib.QueryComplexity.isCertificate_univ` (lemma, [line 290](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L290))

> Reading every coordinate of `x` is a certificate.

```lean
lemma isCertificate_univ (f : BooleanFunction n) (x : BitString n) :
    IsCertificate f x Finset.univ
```

`Cslib.QueryComplexity.filter_isCertificate_nonempty` (lemma, [line 295](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L295))

> There is always a certificate, so `C(f, x)` is a minimum over a non-empty set.

```lean
lemma filter_isCertificate_nonempty (f : BooleanFunction n) (x : BitString n) :
    (Finset.univ.filter (IsCertificate f x)).Nonempty
```

`Cslib.QueryComplexity.certificateComplexityAt` (definition, [line 300](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L300))

> The fewest coordinates of `x` that pin down the value of `f`, denoted `C(f, x)`.

```lean
def certificateComplexityAt (f : BooleanFunction n) (x : BitString n) : ℕ
```

`Cslib.QueryComplexity.certificateComplexityAt_le` (lemma, [line 304](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L304))

> Upper-bound rule for `C(f, x)`: exhibit one certificate.

```lean
lemma certificateComplexityAt_le {f : BooleanFunction n} {x : BitString n} {S : Finset (Fin n)}
    (h : IsCertificate f x S) : certificateComplexityAt f x ≤ S.card
```

`Cslib.QueryComplexity.le_certificateComplexityAt` (lemma, [line 309](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L309))

> Lower-bound rule for `C(f, x)`: a bound that holds for every certificate.

```lean
lemma le_certificateComplexityAt {f : BooleanFunction n} {x : BitString n} {k : ℕ}
    (h : ∀ S, IsCertificate f x S → k ≤ S.card) : k ≤ certificateComplexityAt f x
```

`Cslib.QueryComplexity.exists_isCertificate_card_eq` (theorem, [line 314](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L314))

> Some certificate for `x` has exactly `C(f, x)` coordinates.

```lean
theorem exists_isCertificate_card_eq (f : BooleanFunction n) (x : BitString n) :
    ∃ S, IsCertificate f x S ∧ S.card = certificateComplexityAt f x
```

> ## Certificates as partial assignments
>
> At a fixed input a forcing assignment carries no information beyond the coordinates it reads:
> `Agrees C x` forces `C i = some (x i)` on the support and `none` elsewhere. So `C(f, x)` over
> coordinate sets is also the minimum size of a forcing assignment consistent with `x`.

`Cslib.QueryComplexity.forcingAssignments` (definition, [line 327](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L327))

> Partial assignments consistent with `x` that force `f x`.

```lean
def forcingAssignments (f : BooleanFunction n) (x : BitString n) :
    Finset (PartialAssignment n)
```

`Cslib.QueryComplexity.mem_forcingAssignments` (lemma, [line 332](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L332))

```lean
lemma mem_forcingAssignments {f : BooleanFunction n} {x : BitString n}
    {C : PartialAssignment n} :
    C ∈ forcingAssignments f x ↔ Agrees C x ∧ Forces f C (f x)
```

`Cslib.QueryComplexity.ofBitString_mem_forcingAssignments` (lemma, [line 338](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L338))

> Reading off all of `x` forces `f x`.

```lean
lemma ofBitString_mem_forcingAssignments (f : BooleanFunction n) (x : BitString n) :
    ofBitString x ∈ forcingAssignments f x
```

`Cslib.QueryComplexity.forcingAssignments_nonempty` (lemma, [line 344](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L344))

> There is always a forcing assignment consistent with `x`.

```lean
lemma forcingAssignments_nonempty (f : BooleanFunction n) (x : BitString n) :
    (forcingAssignments f x).Nonempty
```

`Cslib.QueryComplexity.certificateComplexityAt_eq_inf'_size` (theorem, [line 350](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L350))

> `C(f, x)` over coordinate sets is the minimum size of a forcing assignment consistent with
> `x`, the definition of [BuhrmanDeWolf2002].

```lean
theorem certificateComplexityAt_eq_inf'_size (f : BooleanFunction n) (x : BitString n) :
    certificateComplexityAt f x =
      (forcingAssignments f x).inf' (forcingAssignments_nonempty f x) size
```

`Cslib.QueryComplexity.certificateComplexity` (definition, [line 363](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L363))

> The maximum over all inputs of the smallest certificate size, denoted `C(f)`.

```lean
def certificateComplexity (f : BooleanFunction n) : ℕ
```

`Cslib.QueryComplexity.certificateComplexityAt_le_certificateComplexity` (lemma, [line 367](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L367))

> The certificate complexity at a single input is at most that of `f`: `C(f, x) ≤ C(f)`.

```lean
lemma certificateComplexityAt_le_certificateComplexity (f : BooleanFunction n)
    (x : BitString n) : certificateComplexityAt f x ≤ certificateComplexity f
```

`Cslib.QueryComplexity.certificateComplexityAt_le_card` (theorem, [line 372](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L372))

> `C(f, x) ≤ n`: reading every coordinate pins down `f`.

```lean
theorem certificateComplexityAt_le_card (f : BooleanFunction n) (x : BitString n) :
    certificateComplexityAt f x ≤ n
```

`Cslib.QueryComplexity.certificateComplexity_le_card` (theorem, [line 377](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L377))

> `C(f) ≤ n`.

```lean
theorem certificateComplexity_le_card (f : BooleanFunction n) : certificateComplexity f ≤ n
```

> ## `bs(f) ≤ C(f)`
>
> A certificate for `x` must meet every block of a sensitive family. The blocks are pairwise
> disjoint, so a family has at most `|S|` members.

`Cslib.QueryComplexity.sensitiveBlock_inter_nonempty` (theorem, [line 387](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L387))

> A certificate must contain at least one coordinate of every sensitive block.

```lean
theorem sensitiveBlock_inter_nonempty {f : BooleanFunction n} {x : BitString n} {B : Block n}
    (hB : IsSensitiveBlock f x B) {S : Finset (Fin n)} (hS : IsCertificate f x S) :
    (B ∩ S).Nonempty
```

`Cslib.QueryComplexity.card_le_card_of_isSensitiveFamily` (lemma, [line 396](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L396))

> A certificate is at least as large as any sensitive family.

```lean
lemma card_le_card_of_isSensitiveFamily {f : BooleanFunction n} {x : BitString n}
    {F : Finset (Block n)} {S : Finset (Fin n)}
    (hF : IsSensitiveFamily f x F) (hS : IsCertificate f x S) : F.card ≤ S.card
```

`Cslib.QueryComplexity.blockSensitivityAt_le_certificateComplexityAt` (theorem, [line 406](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L406))

> Pointwise: `bs(f, x) ≤ C(f, x)`.

```lean
theorem blockSensitivityAt_le_certificateComplexityAt (f : BooleanFunction n)
    (x : BitString n) : blockSensitivityAt f x ≤ certificateComplexityAt f x
```

`Cslib.QueryComplexity.blockSensitivity_le_certificateComplexity` (theorem, [line 412](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L412))

> Every block of a sensitive family meets every certificate, so `bs(f) ≤ C(f)`.

```lean
theorem blockSensitivity_le_certificateComplexity (f : BooleanFunction n) :
    blockSensitivity f ≤ certificateComplexity f
```

`Cslib.QueryComplexity.blockSensitivityAt_le_card` (theorem, [line 418](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L418))

> `bs(f, x) ≤ n`.

```lean
theorem blockSensitivityAt_le_card (f : BooleanFunction n) (x : BitString n) :
    blockSensitivityAt f x ≤ n
```

`Cslib.QueryComplexity.blockSensitivity_le_card` (theorem, [line 423](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean#L423))

> `bs(f) ≤ n`.

```lean
theorem blockSensitivity_le_card (f : BooleanFunction n) : blockSensitivity f ≤ n
```

## Depends on

- [Boolean functions on the hypercube](defs.md)

## Sources

- [Cslib/Computability/QueryComplexity/Measures.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/QueryComplexity/Measures.lean)
