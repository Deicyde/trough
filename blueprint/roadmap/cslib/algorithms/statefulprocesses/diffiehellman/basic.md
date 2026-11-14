---
catalog: module
lean: Cslib.Algorithms.StatefulProcesses.DiffieHellman.Params, Cslib.Algorithms.StatefulProcesses.DiffieHellman.computePublicMessage, Cslib.Algorithms.StatefulProcesses.DiffieHellman.computeSharedSecret, Cslib.Algorithms.StatefulProcesses.DiffieHellman.computePublicMessage_computeSharedSecret_eq, Cslib.Algorithms.StatefulProcesses.DiffieHellman.FunId, Cslib.Algorithms.StatefulProcesses.DiffieHellman.Params.Val, Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceComputeMesg, Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceComputeSharedSecret, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobComputeMesg, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobComputeSharedSecret, Cslib.Algorithms.StatefulProcesses.DiffieHellman.alice, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bob, Cslib.Algorithms.StatefulProcesses.DiffieHellman.funEval, Cslib.Algorithms.StatefulProcesses.DiffieHellman.net, Cslib.Algorithms.StatefulProcesses.DiffieHellman.alice₁, Cslib.Algorithms.StatefulProcesses.DiffieHellman.alice₂, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bob₁, Cslib.Algorithms.StatefulProcesses.DiffieHellman.bob₂, Cslib.Algorithms.StatefulProcesses.DiffieHellman.Params.cfgLts
statement: formalized
proof: formalized
---

# Diffie-Hellman Key Exchange in Stateful Processes (testbed)

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.Basic`, in [Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean), by Fabrizio Montesi.

> This module formalises the Diffie-Hellman key exchange protocol in `StatefulProcesses`.
>
> It is also intended as a simple testbed to measure improvement on how CSLib deals with embedded DSLs
> like Stateful Processes and reasoning on operational semantics.
>
> Current aspects that stand out and could be more ergonomic are:
> 1. The integration of Lean terms within expressions for computation at processes requires
>   significant plumbing. Ideally, it should be seamless.
> 2. The protocol has two obvious symbolic traces, yet proving `net_completeTraces` is cumbersome.
>   Perhaps an API for unique transitions could be partially helpful:
> ```
> def _root_.Cslib.LTS.TrUnique (lts : LTS State Label) (s : State) (μ : Label) (s' : State) :=
>   lts.Tr s μ s' ∧ ∀ μ' s'', lts.Tr s μ' s'' → μ' = μ ∧ s'' = s'
> ```
>   The terms for `Alice` and `Bob` after one and two steps of their executions are provided as
>   reference for this endeavour.
> 3. As a consequence of (2), proving `net_fun_correct` is cumbersome.
>
> ## Implementation notes
>
> The current implementation requires proofs that `p` is prime and that `g` is a primitive root modulo
> `p`, but does not use these facts. …

> ## Basics

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.Params` (structure, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L50))

> Parameters of the DH protocol.

```lean
structure Params (Pid Var : Type*) where
  /-- Alice. -/
  alice : Pid
  /-- Bob. -/
  bob : Pid
  /-- Alice and Bob have different names. -/
  alice_neq_bob : alice ≠ bob
  /-- Alice's private key (secret). -/
  a : ℕ
  /-- Bob's private key (secret). -/
  b : ℕ
  /-- Bob's variable to store Alice's message. -/
  x : Var
  /-- Alice's variable to store Bob's message. -/
  y : Var
  /-- The variable used to store the shared key. -/
  s : Var
  /-- The prime modulus `p`. -/
  p : ℕ
  /-- `p` is prime. -/
  p_prime : Nat.Prime p
  /-- The generator `g`. -/
  g : ZMod p
  /-- `g` is a primitive root modulo `p`. -/
  g_primitive_root_p : IsPrimitiveRoot g (p - 1)
  /-- SelLabel type for instantiating stateful processes. -/
  SelLabel : Type*
  /-- ProcName type for instantiating stateful processes. -/
  ProcName : Type*
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.computePublicMessage` (definition, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L83))

> Computes the public DH message from a private exponent.

```lean
def computePublicMessage (p : ℕ) (g : ZMod p) (privateExp : ℕ) : ZMod p
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.computeSharedSecret` (definition, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L87))

> Computes the shared secret key from a private exponent and the other party's public message.

```lean
def computeSharedSecret (p : ℕ) (msg : ZMod p) (privateExp : ℕ) : ZMod p
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.computePublicMessage_computeSharedSecret_eq` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L92))

> Correctness of the DH computations: the encryption keys independently computed by the two
> participants are the same.

```lean
theorem computePublicMessage_computeSharedSecret_eq (p : ℕ) (g : ZMod p) (a b : ℕ) :
    computeSharedSecret p (computePublicMessage p g b) a =
    computeSharedSecret p (computePublicMessage p g a) b
```

> ## Behaviour

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.FunId` (inductive type, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L103))

> Function identifiers used in DH.

```lean
inductive FunId | computePublicMessage | computeSharedSecret
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.Params.Val` (inductive type, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L106))

> Value type for DH.

```lean
inductive Params.Val | nat (n : ℕ) | zMod (z : ZMod params.p)
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceComputeMesg` (abbreviation, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L109))

> Alice's expression for computing the public message.

```lean
abbrev aliceComputeMesg : Expr Var params.Val FunId
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.aliceComputeSharedSecret` (abbreviation, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L114))

> Alice's expression for computing the shared secret.

```lean
abbrev aliceComputeSharedSecret : Expr Var params.Val FunId
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobComputeMesg` (abbreviation, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L118))

> Bob's expression for computing the public message.

```lean
abbrev bobComputeMesg : Expr Var params.Val FunId
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bobComputeSharedSecret` (abbreviation, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L123))

> Bob's expression for computing the shared secret.

```lean
abbrev bobComputeSharedSecret : Expr Var params.Val FunId
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.alice` (definition, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L127))

> Alice's program.

```lean
def alice : Process Pid Var params.Val FunId params.SelLabel params.ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bob` (definition, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L134))

> Bob's program.

```lean
def bob : Process Pid Var params.Val FunId params.SelLabel params.ProcName
```

> ## Semantics

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.funEval` (definition, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L144))

> Implementation of local function call evaluation.
> Calls with a mismatched modulus are rejected.

```lean
def funEval : FunCallEval FunId params.Val
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.net` (definition, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L152))

> DH network.

```lean
def net [DecidableEq Pid] : Network Pid Var params.Val FunId params.SelLabel params.ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.alice₁` (definition, [line 159](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L159))

> Alice's program after one step.

```lean
def alice₁ : Process Pid Var params.Val FunId params.SelLabel params.ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.alice₂` (definition, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L164))

> Alice's program after two steps.

```lean
def alice₂ : Process Pid Var params.Val FunId params.SelLabel params.ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bob₁` (definition, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L169))

> Bob's program after one step.

```lean
def bob₁ : Process Pid Var params.Val FunId params.SelLabel params.ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.bob₂` (definition, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L174))

> Bob's program after two steps.

```lean
def bob₂ : Process Pid Var params.Val FunId params.SelLabel params.ProcName
```

`Cslib.Algorithms.StatefulProcesses.DiffieHellman.Params.cfgLts` (abbreviation, [line 194](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean#L194))

> The LTS of network configurations.

```lean
abbrev Params.cfgLts {SelLabel ProcName : Type*}
```

## Depends on

- [Networks of stateful processes and their semantics](../../../languages/statefulprocesses/network.md)

## Sources

- [Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/StatefulProcesses/DiffieHellman/Basic.lean)
