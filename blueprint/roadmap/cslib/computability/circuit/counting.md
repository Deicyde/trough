---
catalog: module
lean: Cslib.Circuits.computableFunctions, Cslib.Circuits.mem_computableFunctions, Cslib.Circuits.mem_computableFunctions_iff_ecomplexity_le, Cslib.Circuits.irredundantFunctions, Cslib.Circuits.mem_irredundantFunctions, Cslib.Circuits.card_irredundantFunctions_mul_factorial_le, Cslib.Circuits.card_computableFunctions_le_sum, Cslib.Circuits.card_computableFunctions_mul_factorial_le, Cslib.Circuits.card_computableFunctions_mul_factorial_le_of_arity_le, Cslib.Circuits.fullBasisLineBound, Cslib.Circuits.card_computableFunctions_full_mul_factorial_le
statement: formalized
proof: formalized
---

# Counting functions computed by finite circuits

`Cslib.Computability.Circuit.Counting`, in [Cslib/Computability/Circuit/Counting.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean), by Samuel Schlesinger.

> For a finite signature, only finitely many functions can be computed with a fixed gate budget,
> even when the carrier is infinite. The set `computableFunctions I n s` of scalar functions whose
> `ecomplexity` is at most `s` is covered by the outputs of the finitely many programs of each
> size, so it is finite and its cardinality is `Set.ncard`. Semantic equality and normalization
> use classical reasoning.
>
> After merging gates that compute the same function, a circuit with `g` gates has `g!` distinct
> labeled presentations. This factorial correction sharpens the count used in Shannon's lower bound.
> The main bound accepts any uniform bound on the number of lines;
> `card_computableFunctions_mul_factorial_le_of_arity_le` specializes it to operation arities.
> `card_computableFunctions_full_mul_factorial_le` uses the exact full-basis line count,
> keeping the number of operation tables explicit when the arity varies.

`Cslib.Circuits.computableFunctions` (definition, [line 52](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L52))

> Scalar functions computable with at most `s` gates.

```lean
def computableFunctions (I : Interpretation σ U) (n s : ℕ) : Set ((Fin n → U) → U)
```

`Cslib.Circuits.mem_computableFunctions` (theorem, [line 55](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L55))

```lean
theorem mem_computableFunctions {f : (Fin n → U) → U} :
    f ∈ computableFunctions I n s ↔
      ∃ c : Circuit σ n 1, c.Computes I (single f) ∧ c.size ≤ s
```

`Cslib.Circuits.mem_computableFunctions_iff_ecomplexity_le` (theorem, [line 61](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L61))

> The functions computable with at most `s` gates are those of complexity at most `s`.

```lean
theorem mem_computableFunctions_iff_ecomplexity_le {f : (Fin n → U) → U} :
    f ∈ computableFunctions I n s ↔ ecomplexity I (single f) ≤ s
```

`Cslib.Circuits.irredundantFunctions` (definition, [line 78](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L78))

> Functions computed by a circuit whose `g` gates compute pairwise distinct functions.
> Permuting the gates of such a circuit, ignoring their order, gives `g!` distinct gate lists;
> this is the factorial saving in the counting bound.

```lean
def irredundantFunctions (I : Interpretation σ U) (n g : ℕ) : Set ((Fin n → U) → U)
```

`Cslib.Circuits.mem_irredundantFunctions` (theorem, [line 81](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L81))

```lean
theorem mem_irredundantFunctions {f : (Fin n → U) → U} :
    f ∈ irredundantFunctions I n g ↔
      ∃ c : Circuit σ n 1, c.Computes I (single f) ∧ c.Irredundant I ∧ c.size = g
```

`Cslib.Circuits.card_irredundantFunctions_mul_factorial_le` (theorem, [line 174](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L174))

> Distinct functions and permutations of their irredundant gates give distinct presentations.

```lean
theorem card_irredundantFunctions_mul_factorial_le (I : Interpretation σ U) (n g : ℕ) :
    (irredundantFunctions I n g).ncard * g.factorial ≤
      card (Line σ n g) ^ g * (n + g)
```

`Cslib.Circuits.card_computableFunctions_le_sum` (theorem, [line 183](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L183))

> Normalizing a circuit with at most `s` gates leaves an irredundant circuit with at most `s`
> gates computing the same function.

```lean
theorem card_computableFunctions_le_sum (I : Interpretation σ U) (n s : ℕ) :
    (computableFunctions I n s).ncard ≤
      ∑ g ∈ Finset.range (s + 1), (irredundantFunctions I n g).ncard
```

`Cslib.Circuits.card_computableFunctions_mul_factorial_le` (theorem, [line 207](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L207))

> Bound the number of computable functions using a uniform line count `B`. The condition
> `s ≤ B` absorbs the extra factorial factors from circuits with fewer than `s` gates.

```lean
theorem card_computableFunctions_mul_factorial_le (I : Interpretation σ U) (n s B : ℕ)
    (hB : s ≤ B) (hlines : ∀ g ≤ s, card (Line σ n g) ≤ B) :
    (computableFunctions I n s).ncard * s.factorial ≤
      (s + 1) * B ^ s * (n + s)
```

`Cslib.Circuits.card_computableFunctions_mul_factorial_le_of_arity_le` (theorem, [line 234](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L234))

> A cardinality bound for any finite signature with bounded arities. The maximum also
> covers empty signatures and signatures containing only nullary operations.

```lean
theorem card_computableFunctions_mul_factorial_le_of_arity_le
    (I : Interpretation σ U) (n s r : ℕ) (arity_le : ∀ op, σ.Arity op ≤ r) :
    (computableFunctions I n s).ncard * s.factorial ≤
      (s + 1) * (max s (card σ.Op * (n + s + 1) ^ r)) ^ s * (n + s)
```

`Cslib.Circuits.fullBasisLineBound` (abbreviation, [line 246](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L246))

> A uniform line budget for full-basis circuits with carrier size `q`, arity `k`,
> `n` inputs, and at most `s` gates. The maximum absorbs the factorial correction.

```lean
abbrev fullBasisLineBound (q k n s : ℕ) : ℕ
```

`Cslib.Circuits.card_computableFunctions_full_mul_factorial_le` (theorem, [line 251](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean#L251))

> The full-basis count keeps the number of operation tables explicit, so the arity may
> vary along with the number of inputs and the gate budget.

```lean
theorem card_computableFunctions_full_mul_factorial_le [Finite U]
    (k n s : ℕ) :
    (computableFunctions (fullInterpretation (k := k) (Carrier := U)) n s).ncard * s.factorial ≤
      (s + 1) * fullBasisLineBound (card U) k n s ^ s * (n + s)
```

## Depends on

- [Circuit complexity](complexity.md)
- [Semantic circuit normalization](normalization.md)

## Proof depends on

- [Finite circuit syntax](finite.md)

## Sources

- [Cslib/Computability/Circuit/Counting.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Counting.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Computability.Circuit.Counting.json)
