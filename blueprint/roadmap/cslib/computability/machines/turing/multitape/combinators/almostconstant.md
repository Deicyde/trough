---
catalog: module
lean: Turing.MultiTapeTM.encPrefixes, Turing.MultiTapeTM.mem_encPrefixes, Turing.MultiTapeTM.prefix_mem_encPrefixes, Turing.MultiTapeTM.outSuffixes, Turing.MultiTapeTM.suffix_out_mem_outSuffixes, Turing.MultiTapeTM.mem_outSuffixes, Turing.MultiTapeTM.suffix_mem_outSuffixes, Turing.MultiTapeTM.tail_mem_outSuffixes, Turing.MultiTapeTM.encOut_mem_outSuffixes, Turing.MultiTapeTM.AlmostConstState, Turing.MultiTapeTM.encodedFun, Turing.MultiTapeTM.encodedFun_enc, Turing.MultiTapeTM.encodedFun_enc_of_notMem, Turing.MultiTapeTM.encodedFun_mem_outSuffixes, Turing.MultiTapeTM.almostConstTM, Turing.MultiTapeTM.runFrom_read, Turing.MultiTapeTM.runFrom_write, Turing.MultiTapeTM.runFrom_write_halted, Turing.MultiTapeTM.almostConstTime, Turing.MultiTapeTM.length_le_sup_of_mem_encPrefixes, Turing.MultiTapeTM.reaches_write, Turing.MultiTapeTM.computesFunInTimeAndSpace_almostConstTM, Turing.MultiTapeTM.computableInTimeAndSpace_almostConstTime, Turing.MultiTapeTM.computableInTimeAndSpace_of_exists_finite_ne, Turing.MultiTapeTM.computableInTimeAndSpace_of_const, Turing.MultiTapeTM.finiteFunTime, Turing.MultiTapeTM.computableInTimeAndSpace_finiteFunTime, Turing.MultiTapeTM.computableInTimeAndSpace_of_finite
statement: formalized
proof: formalized
---

# Complexity of Almost Constant Functions

`Cslib.Computability.Machines.Turing.MultiTape.Combinators.AlmostConstant`, in [Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean), by Christian Reitwiessner.

> A function `f : α → β` that is constant except for a finite number of arguments is computable in
> constant time and zero space: the machine reads the encoded input while remembering the prefix it
> has seen so far. After a finite number of steps it either reaches the end of the input or a point
> where the prefix cannot be extended to the encoding of one of the finitely many exceptions. In both
> cases, it emits the corresponding output one symbol at a time.
>
> This result also holds for functions whose domain is already finite.
>
> ## Main Results
>
> * `encodedComputableInTimeAndSpace_of_finite`: Every function on a finite type is computable in
>     constant time and zero space, relative to any encoding.
> * `encodedComputableInTimeAndSpace_of_exists_finite_ne`: Every function that is constant except
>     for a finite number of arguments is computable in constant time and zero space, relative to any
>     encoding.
> * `encodedComputableInTimeAndSpace_of_const`: Every constant function is computable in constant
>     time and zero space, relative to any encoding.
> * `encodedComputableInTimeAndSpace_almostConstTime` and
>     `encodedComputableInTimeAndSpace_finiteFunTime`: The same with explicit time bounds.

> ## The machine computing a function that is constant outside a finite set
>
> The machine `almostConstTM encIn encOut f S out` computes `f`, provided that the encoded output
> of `f` is the fixed Boolean string `out` outside of the finite set `S`.

`Turing.MultiTapeTM.encPrefixes` (definition, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L55))

> The prefixes of the encodings of the elements of a finite set `S`, together with the empty list.
>
> The empty list has to be added explicitly for the case where `S` is empty: `almostConstTM` uses
> the elements of this set as its states while reading the input, so the set has to contain the
> starting state `[]` even if there is nothing to distinguish.

```lean
def encPrefixes (encIn : α ↪ List Bool) (S : Finset α) : Finset (List Bool)
```

`Turing.MultiTapeTM.mem_encPrefixes` (lemma, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L58))

```lean
lemma mem_encPrefixes {p : List Bool} {a : α} (ha : a ∈ S) (h : p <+: encIn a) :
    p ∈ encPrefixes encIn S
```

`Turing.MultiTapeTM.prefix_mem_encPrefixes` (lemma, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L64))

> The set of prefixes is closed under taking prefixes.

```lean
lemma prefix_mem_encPrefixes {p q : List Bool} (h : p ∈ encPrefixes encIn S) (hq : q <+: p) :
    q ∈ encPrefixes encIn S
```

`Turing.MultiTapeTM.outSuffixes` (definition, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L73))

> The suffixes of the default output and of the encoded values of `f` on `S`.

```lean
def outSuffixes (encOut : β ↪ List Bool) (f : α → β) (S : Finset α) (out : List Bool) :
    Finset (List Bool)
```

`Turing.MultiTapeTM.suffix_out_mem_outSuffixes` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L77))

```lean
lemma suffix_out_mem_outSuffixes {w : List Bool} (h : w <:+ out) :
    w ∈ outSuffixes encOut f S out
```

`Turing.MultiTapeTM.mem_outSuffixes` (lemma, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L82))

```lean
lemma mem_outSuffixes {w : List Bool} {a : α} (ha : a ∈ S) (h : w <:+ encOut (f a)) :
    w ∈ outSuffixes encOut f S out
```

`Turing.MultiTapeTM.suffix_mem_outSuffixes` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L88))

> The set of suffixes is closed under taking suffixes.

```lean
lemma suffix_mem_outSuffixes {v w : List Bool} (h : w ∈ outSuffixes encOut f S out) (hv : v <:+ w) :
    v ∈ outSuffixes encOut f S out
```

`Turing.MultiTapeTM.tail_mem_outSuffixes` (lemma, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L96))

```lean
lemma tail_mem_outSuffixes {w : List Bool} (h : w ∈ outSuffixes encOut f S out) :
    w.tail ∈ outSuffixes encOut f S out
```

`Turing.MultiTapeTM.encOut_mem_outSuffixes` (lemma, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L102))

> If the encoded output is the default output outside of `S`, then every encoded output occurs
> among the suffixes.

```lean
lemma encOut_mem_outSuffixes (h : ∀ a ∉ S, encOut (f a) = out) (a : α) :
    encOut (f a) ∈ outSuffixes encOut f S out
```

`Turing.MultiTapeTM.AlmostConstState` (abbreviation, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L111))

> The states of the machine `almostConstTM`: either the prefix of the input read so far, or the
> part of the output that still has to be emitted.

```lean
abbrev AlmostConstState (encIn : α ↪ List Bool) (encOut : β ↪ List Bool) (f : α → β)
    (S : Finset α) (out : List Bool) : Type
```

`Turing.MultiTapeTM.encodedFun` (definition, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L119))

> The function `f`, transported along the encodings of its domain and codomain: it maps the
> encoding of an element of `S` to the encoding of its value under `f`, and every other list to the
> default output.

```lean
noncomputable def encodedFun (encIn : α ↪ List Bool) (encOut : β ↪ List Bool) (f : α → β)
    (S : Finset α) (out : List Bool) (p : List Bool) : List Bool
```

`Turing.MultiTapeTM.encodedFun_enc` (lemma, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L124))

```lean
lemma encodedFun_enc {a : α} (ha : a ∈ S) :
    encodedFun encIn encOut f S out (encIn a) = encOut (f a)
```

`Turing.MultiTapeTM.encodedFun_enc_of_notMem` (lemma, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L130))

```lean
lemma encodedFun_enc_of_notMem {a : α} (ha : a ∉ S) :
    encodedFun encIn encOut f S out (encIn a) = out
```

`Turing.MultiTapeTM.encodedFun_mem_outSuffixes` (lemma, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L137))

```lean
lemma encodedFun_mem_outSuffixes (p : List Bool) :
    encodedFun encIn encOut f S out p ∈ outSuffixes encOut f S out
```

`Turing.MultiTapeTM.almostConstTM` (definition, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L151))

> The machine computing a function that is constant outside of `S`. It has no work tapes.
>
> While reading the input it remembers the prefix read so far. Once this prefix cannot be extended
> to the encoding of an element of `S` anymore, or the blank behind the input is reached, it
> switches to the state that holds the encoded output, which it then emits one symbol per step
> before halting.

```lean
noncomputable def almostConstTM (encIn : α ↪ List Bool) (encOut : β ↪ List Bool) (f : α → β)
    (S : Finset α) (out : List Bool) :
    MultiTapeTM 0 Bool (AlmostConstState encIn encOut f S out)
```

`Turing.MultiTapeTM.runFrom_read` (lemma, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L174))

> The configuration reached after `j` steps of reading the input.

```lean
lemma runFrom_read (a : α) {j : ℕ} (hj : j ≤ (encIn a).length)
    (hmem : (encIn a).take j ∈ encPrefixes encIn S) :
    (almostConstTM encIn encOut f S out).runFrom
        ((almostConstTM encIn encOut f S out).initCfg (encIn a)) j =
      { state := some (Sum.inl ⟨(encIn a).take j, hmem⟩),
        inputPos := ⟨1 + j, by omega⟩,
        workTapes := fun _ _ => none,
        workTapePos := fun _ => 0,
        output := [] }
```

`Turing.MultiTapeTM.runFrom_write` (lemma, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L208))

> The configuration reached after having emitted the first `i` symbols of `w`, starting from a
> configuration that is about to emit `w`.

```lean
lemma runFrom_write {input : List Bool} (pos : Fin (input.length + 2)) (o : List Bool)
    {w : List Bool} (hw : w ∈ outSuffixes encOut f S out) {i : ℕ} (hi : i ≤ w.length) :
    (almostConstTM encIn encOut f S out).runFrom
        { state := some (Sum.inr ⟨w, hw⟩), inputPos := pos, workTapes := fun _ _ => none,
          workTapePos := fun _ => 0, output := o } i =
      { state := some (Sum.inr ⟨w.drop i, suffix_mem_outSuffixes hw (w.drop_suffix i)⟩),
        inputPos := pos,
        workTapes := fun _ _ => none,
        workTapePos := fun _ => 0,
        output := o ++ w.take i }
```

`Turing.MultiTapeTM.runFrom_write_halted` (lemma, [line 234](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L234))

> Starting from a configuration that is about to emit `w`, the machine halts after `w.length + 1`
> steps, having emitted `w`.

```lean
lemma runFrom_write_halted {input : List Bool} (pos : Fin (input.length + 2)) (o : List Bool)
    {w : List Bool} (hw : w ∈ outSuffixes encOut f S out) :
    (almostConstTM encIn encOut f S out).runFrom
        { state := some (Sum.inr ⟨w, hw⟩), inputPos := pos, workTapes := fun _ _ => none,
          workTapePos := fun _ => 0, output := o } (w.length + 1) =
      { state := none,
        inputPos := pos,
        workTapes := fun _ _ => none,
        workTapePos := fun _ => 0,
        output := o ++ w }
```

`Turing.MultiTapeTM.almostConstTime` (definition, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L252))

> A constant time bound for the machine `almostConstTM`.

```lean
public def almostConstTime (encIn : α ↪ List Bool) (encOut : β ↪ List Bool) (f : α → β)
    (S : Finset α) (out : List Bool) : ℕ
```

`Turing.MultiTapeTM.length_le_sup_of_mem_encPrefixes` (lemma, [line 256](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L256))

```lean
lemma length_le_sup_of_mem_encPrefixes {p : List Bool} (h : p ∈ encPrefixes encIn S) :
    p.length ≤ S.sup fun a => (encIn a).length + (encOut (f a)).length
```

`Turing.MultiTapeTM.reaches_write` (lemma, [line 270](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L270))

> The machine reaches the state in which it starts emitting the encoded output after a number
> of steps that is bounded independently of the input.

```lean
lemma reaches_write (h : ∀ a ∉ S, encOut (f a) = out) (a : α) :
    ∃ (j : ℕ) (hj : j ≤ (encIn a).length),
      j + (encOut (f a)).length ≤
        out.length + S.sup (fun a => (encIn a).length + (encOut (f a)).length) ∧
      (almostConstTM encIn encOut f S out).runFrom
          ((almostConstTM encIn encOut f S out).initCfg (encIn a)) (j + 1) =
        { state := some (Sum.inr ⟨encOut (f a), encOut_mem_outSuffixes h a⟩),
          inputPos := ⟨1 + j, by omega⟩,
          workTapes := fun _ _ => none,
          workTapePos := fun _ => 0,
          output := [] }
```

`Turing.MultiTapeTM.computesFunInTimeAndSpace_almostConstTM` (lemma, [line 326](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L326))

> The machine `almostConstTM` computes `f` in at most `almostConstTime` steps and no space.

```lean
lemma computesFunInTimeAndSpace_almostConstTM (h : ∀ a ∉ S, encOut (f a) = out) :
    (almostConstTM encIn encOut f S out).ComputesFunInTimeAndSpace encIn encOut f
      (fun _ => almostConstTime encIn encOut f S out) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_almostConstTime` (theorem, [line 346](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L346))

> Every function whose encoded output is constant outside of a finite set is computable in time
> `almostConstTime` and zero space.

```lean
public theorem computableInTimeAndSpace_almostConstTime
    (f : α → β) (S : Finset α) (out : List Bool) (h : ∀ a ∉ S, encOut (f a) = out) :
    ComputableInTimeAndSpace f encIn encOut
      (fun _ => almostConstTime encIn encOut f S out) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_exists_finite_ne` (theorem, [line 354](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L354))

> Every almost constant function is computable in constant time and zero space.

```lean
public theorem computableInTimeAndSpace_of_exists_finite_ne
    {f : α → β} (h : ∃ b : β, {a : α | f a ≠ b}.Finite) :
    ∃ c, ComputableInTimeAndSpace f encIn encOut (fun _ => c) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_const` (theorem, [line 364](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L364))

> Every constant function is computable in constant time and zero space.

```lean
public theorem computableInTimeAndSpace_of_const {α β : Type*}
    {encIn : α ↪ List Bool} {encOut : β ↪ List Bool} (b : β) :
    ∃ c, ComputableInTimeAndSpace (Function.const α b) encIn encOut
      (fun _ => c) (fun _ => 0)
```

`Turing.MultiTapeTM.finiteFunTime` (definition, [line 372](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L372))

> A constant time bound for functions on a finite type.

```lean
public noncomputable def finiteFunTime {α β : Type*} [Finite α] (encIn : α ↪ List Bool)
    (encOut : β ↪ List Bool) (f : α → β) : ℕ
```

`Turing.MultiTapeTM.computableInTimeAndSpace_finiteFunTime` (theorem, [line 378](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L378))

> Every function on a finite type is computable in time `finiteFunTime` and zero space.

```lean
public theorem computableInTimeAndSpace_finiteFunTime {α β : Type*} [Finite α]
    {encIn : α ↪ List Bool} {encOut : β ↪ List Bool} (f : α → β) :
    ComputableInTimeAndSpace f encIn encOut
      (fun _ => finiteFunTime encIn encOut f) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_finite` (theorem, [line 386](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L386))

> Every function on a finite type is computable in constant time and zero space.

```lean
public theorem computableInTimeAndSpace_of_finite {α β : Type*} [Finite α]
    {encIn : α ↪ List Bool} {encOut : β ↪ List Bool}
    (f : α → β) :
    ∃ c, ComputableInTimeAndSpace f encIn encOut (fun _ => c) (fun _ => 0)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean)
