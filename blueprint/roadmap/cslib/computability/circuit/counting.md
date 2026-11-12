---
catalog: module
lean: Cslib.Circuits.computableFunctions, Cslib.Circuits.mem_computableFunctions, Cslib.Circuits.mem_computableFunctions_iff_ecomplexity_le, Cslib.Circuits.irredundantFunctions, Cslib.Circuits.mem_irredundantFunctions, Cslib.Circuits.card_irredundantFunctions_mul_factorial_le, Cslib.Circuits.card_computableFunctions_le_sum, Cslib.Circuits.card_computableFunctions_mul_factorial_le, Cslib.Circuits.card_computableFunctions_mul_factorial_le_of_arity_le
statement: formalized
proof: formalized
---

# Counting functions computed by finite circuits

`Cslib.Computability.Circuit.Counting`, in [Cslib/Computability/Circuit/Counting.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean), by Samuel Schlesinger.

> For a finite signature, only finitely many functions can be computed with a fixed gate budget,
> even when the carrier is infinite. We enumerate the programs of each size together with an
> output wire and collect the scalar functions they compute, so that `computableFunctions I n s`
> is the finite set of functions whose `ecomplexity` is at most `s`. Semantic equality and
> normalization use classical reasoning, as does choosing an enumeration of the finite syntax.
>
> After merging gates that compute the same function, a circuit with `g` gates has `g!` distinct
> labeled presentations. This factorial correction sharpens the count used in Shannon's lower bound.
> The main bound accepts any uniform bound on the number of lines;
> `card_computableFunctions_mul_factorial_le_of_arity_le` specializes it to operation arities.

`Cslib.Circuits.computableFunctions` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L49))

> Scalar functions computable with at most `s` gates. Enumerating the programs of each size
> with an output wire makes this set finite without requiring a finite carrier.

```lean
noncomputable def computableFunctions (I : Interpretation σ U) (n s : ℕ) :
    Finset ((Fin n → U) → U)
```

`Cslib.Circuits.mem_computableFunctions` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L56))

```lean
theorem mem_computableFunctions {f : (Fin n → U) → U} :
f ∈ computableFunctions I n s ↔
∃ c : Circuit σ n 1, c.Computes I (single f) ∧ c.size ≤ s
```

`Cslib.Circuits.mem_computableFunctions_iff_ecomplexity_le` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L68))

> The functions computable with at most `s` gates are those of complexity at most `s`.

```lean
theorem mem_computableFunctions_iff_ecomplexity_le {f : (Fin n → U) → U} :
    f ∈ computableFunctions I n s ↔ ecomplexity I (single f) ≤ s
```

`Cslib.Circuits.irredundantFunctions` (definition, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L75))

> Functions computed at an output wire of a program whose `g` gates compute pairwise distinct
> functions. Permuting the gates of such a program, ignoring their order, gives `g!` distinct gate
> lists; this is the factorial saving in the counting bound.

```lean
noncomputable def irredundantFunctions (I : Interpretation σ U) (n g : ℕ) :
    Finset ((Fin n → U) → U)
```

`Cslib.Circuits.mem_irredundantFunctions` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L87))

```lean
theorem mem_irredundantFunctions {f : (Fin n → U) → U} :
f ∈ irredundantFunctions I n g ↔
∃ c : Circuit σ n 1, c.Computes I (single f) ∧ c.Irredundant I ∧ c.size = g
```

`Cslib.Circuits.card_irredundantFunctions_mul_factorial_le` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L172))

> Distinct functions and permutations of their irredundant gates give distinct presentations.

```lean
theorem card_irredundantFunctions_mul_factorial_le (I : Interpretation σ U) (n g : ℕ) :
    (irredundantFunctions I n g).card * g.factorial ≤
      Nat.card (Line σ n g) ^ g * (n + g)
```

`Cslib.Circuits.card_computableFunctions_le_sum` (theorem, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L182))

> Normalizing a circuit with at most `s` gates leaves an irredundant program with at most `s`
> gates computing the same function.

```lean
theorem card_computableFunctions_le_sum (I : Interpretation σ U) (n s : ℕ) :
    (computableFunctions I n s).card ≤
      ∑ g ∈ Finset.range (s + 1), (irredundantFunctions I n g).card
```

`Cslib.Circuits.card_computableFunctions_mul_factorial_le` (theorem, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L198))

> Bound the number of computable functions using a uniform line count `B`. The condition
> `s ≤ B` absorbs the extra factorial factors from circuits with fewer than `s` gates.

```lean
theorem card_computableFunctions_mul_factorial_le (I : Interpretation σ U) (n s B : ℕ)
    (hB : s ≤ B) (hlines : ∀ g ≤ s, Nat.card (Line σ n g) ≤ B) :
    (computableFunctions I n s).card * s.factorial ≤
      (s + 1) * B ^ s * (n + s)
```

`Cslib.Circuits.card_computableFunctions_mul_factorial_le_of_arity_le` (theorem, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean#L225))

> A cardinality bound for any finite signature with bounded arities. The maximum also
> covers empty signatures and signatures containing only nullary operations.

```lean
theorem card_computableFunctions_mul_factorial_le_of_arity_le
    (I : Interpretation σ U) (n s r : ℕ) (arity_le : ∀ op, σ.Arity op ≤ r) :
    (computableFunctions I n s).card * s.factorial ≤
      (s + 1) * (max s (Nat.card σ.Op * (n + s + 1) ^ r)) ^ s * (n + s)
```

## Depends on

- [Circuit complexity](complexity.md)
- [Semantic circuit normalization](normalization.md)

## Proof depends on

- [Finite circuit syntax](finite.md)

## Sources

- [Cslib/Computability/Circuit/Counting.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Counting.lean)
