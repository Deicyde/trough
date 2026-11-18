---
catalog: module
lean: Cslib.URM.Regs.write_read_self, Cslib.URM.Regs.write_read_of_ne, Cslib.URM.State.isHalted_iff, Cslib.URM.State.ext, Cslib.URM.Instr.IsJump, Cslib.URM.Instr.Z_nonJump, Cslib.URM.Instr.S_nonJump, Cslib.URM.Instr.T_nonJump, Cslib.URM.Instr.J_IsJump, Cslib.URM.Instr.shiftJumps_of_nonJump, Cslib.URM.Instr.JumpsBoundedBy, Cslib.URM.Instr.jumpsBoundedBy_of_nonJump, Cslib.URM.Instr.JumpsBoundedBy.mono, Cslib.URM.Instr.JumpsBoundedBy.shiftJumps, Cslib.URM.Instr.capJump, Cslib.URM.Instr.capJump_Z, Cslib.URM.Instr.capJump_S, Cslib.URM.Instr.capJump_T, Cslib.URM.Instr.capJump_J, Cslib.URM.Instr.JumpsBoundedBy.capJump, Cslib.URM.Instr.capJump_idempotent, Cslib.URM.Program.mem_maxRegister
statement: formalized
proof: formalized
---

# URM Basic Lemmas

`Cslib.Computability.URM.Basic`, in [Cslib/Computability/URM/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean), by Jesse Alama.

> This file contains basic lemmas and helper operations for URM types.
>
> ## Main definitions
>
> - `Instr.IsJump`: predicate for jump instructions
> - `Instr.JumpsBoundedBy`: checks if jump targets are bounded
> - `Instr.capJump`: caps jump targets to a given length
>
> ## Main results
>
> - `Regs.write_read_self`, `Regs.write_read_of_ne`: register read/write lemmas
> - `State.isHalted_iff`, `State.ext`: state lemmas
> - `JumpsBoundedBy.mono`: bounded jumps are monotonic in the bound
> - `JumpsBoundedBy.shiftJumps`: shifting preserves bounded jumps
> - `Program.mem_maxRegister`: instruction maxRegister bounded by program maxRegister

> ## Register Lemmas

`Cslib.URM.Regs.write_read_self` (theorem, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L40))

```lean
theorem write_read_self (σ : Regs) (n v : ℕ) : (σ.write n v).read n = v
```

`Cslib.URM.Regs.write_read_of_ne` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L44))

```lean
theorem write_read_of_ne (σ : Regs) (m n v : ℕ) (h : m ≠ n) :
    (σ.write n v).read m = σ.read m
```

> ## State Lemmas

`Cslib.URM.State.isHalted_iff` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L55))

```lean
theorem isHalted_iff (s : State) (p : Program) : s.isHalted p ↔ p.length ≤ s.pc
```

`Cslib.URM.State.ext` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L59))

> Extensionality for State: two states are equal iff their components are equal.

```lean
theorem ext {s₁ s₂ : State} (hpc : s₁.pc = s₂.pc) (hregs : s₁.regs = s₂.regs) : s₁ = s₂
```

> ## Instruction Lemmas

> ## Jump Instructions

`Cslib.URM.Instr.IsJump` (definition, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L71))

> An instruction is a jump instruction.

```lean
def IsJump : Instr → Prop
```

`Cslib.URM.Instr.Z_nonJump` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L80))

> Z instruction is not a jump.

```lean
theorem Z_nonJump (n : ℕ) : ¬(Z n).IsJump
```

`Cslib.URM.Instr.S_nonJump` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L84))

> S instruction is not a jump.

```lean
theorem S_nonJump (n : ℕ) : ¬(S n).IsJump
```

`Cslib.URM.Instr.T_nonJump` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L88))

> T instruction is not a jump.

```lean
theorem T_nonJump (m n : ℕ) : ¬(T m n).IsJump
```

`Cslib.URM.Instr.J_IsJump` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L92))

> J instruction is a jump.

```lean
theorem J_IsJump (m n q : ℕ) : (J m n q).IsJump
```

`Cslib.URM.Instr.shiftJumps_of_nonJump` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L95))

> shiftJumps is identity for non-jumping instructions.

```lean
theorem shiftJumps_of_nonJump {instr : Instr}
    (h : ¬instr.IsJump) (offset : ℕ) : instr.shiftJumps offset = instr
```

> ## Bounded Jump Targets

`Cslib.URM.Instr.JumpsBoundedBy` (definition, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L105))

> An instruction's jump target is bounded by a given length.
> Non-jump instructions trivially satisfy this.

```lean
def JumpsBoundedBy (len : ℕ) : Instr → Prop
```

`Cslib.URM.Instr.jumpsBoundedBy_of_nonJump` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L113))

> Non-jumping instructions have bounded jumps for any length.

```lean
theorem jumpsBoundedBy_of_nonJump {instr : Instr} (h : ¬instr.IsJump)
    (len : ℕ) : instr.JumpsBoundedBy len
```

`Cslib.URM.Instr.JumpsBoundedBy.mono` (theorem, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L120))

> JumpsBoundedBy is monotonic: if bounded for len1, then bounded for any len2 ≥ len1.

```lean
theorem JumpsBoundedBy.mono {instr : Instr} {len1 len2 : ℕ}
    (h : instr.JumpsBoundedBy len1) (hle : len1 ≤ len2) :
    instr.JumpsBoundedBy len2
```

`Cslib.URM.Instr.JumpsBoundedBy.shiftJumps` (theorem, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L126))

> shiftJumps preserves bounded jumps with adjusted bound.

```lean
theorem JumpsBoundedBy.shiftJumps {instr : Instr} {len offset : ℕ}
    (h : instr.JumpsBoundedBy len) :
    (instr.shiftJumps offset).JumpsBoundedBy (offset + len)
```

> ## Jump Target Capping

`Cslib.URM.Instr.capJump` (definition, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L137))

> Cap a jump target to be at most `len`. Non-jump instructions are unchanged.

```lean
def capJump (len : ℕ) : Instr → Instr
```

`Cslib.URM.Instr.capJump_Z` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L144))

```lean
theorem capJump_Z (len n : ℕ) : (Z n).capJump len = Z n
```

`Cslib.URM.Instr.capJump_S` (theorem, [line 147](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L147))

```lean
theorem capJump_S (len n : ℕ) : (S n).capJump len = S n
```

`Cslib.URM.Instr.capJump_T` (theorem, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L150))

```lean
theorem capJump_T (len m n : ℕ) : (T m n).capJump len = T m n
```

`Cslib.URM.Instr.capJump_J` (theorem, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L153))

```lean
theorem capJump_J (len m n q : ℕ) :
    (J m n q).capJump len = J m n (min q len)
```

`Cslib.URM.Instr.JumpsBoundedBy.capJump` (theorem, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L157))

> capJump always produces an instruction with bounded jump.

```lean
theorem JumpsBoundedBy.capJump (len : ℕ) (instr : Instr) :
    (instr.capJump len).JumpsBoundedBy len
```

`Cslib.URM.Instr.capJump_idempotent` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L165))

> capJump is idempotent: capping twice is the same as capping once.

```lean
theorem capJump_idempotent (len : ℕ) (instr : Instr) :
    (instr.capJump len).capJump len = instr.capJump len
```

`Cslib.URM.Program.mem_maxRegister` (theorem, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean#L176))

> Any instruction in a program has maxRegister at most the program's maxRegister.

```lean
theorem mem_maxRegister {p : Program} {instr : Instr} (h : instr ∈ p) :
    instr.maxRegister ≤ p.maxRegister
```

## Depends on

- [URM Core Definitions](defs.md)

## Sources

- [Cslib/Computability/URM/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Basic.lean)
