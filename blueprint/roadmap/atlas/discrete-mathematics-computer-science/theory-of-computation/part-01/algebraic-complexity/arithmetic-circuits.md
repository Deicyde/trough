---
declaration: section
origin: cited
lean: Cslib.Complexity.Algebraic.ArithmeticOperand, Cslib.Complexity.Algebraic.ArithmeticGate, Cslib.Complexity.Algebraic.ArithmeticCircuit, Cslib.Complexity.Algebraic.ArithmeticOperand.evaluate, Cslib.Complexity.Algebraic.ArithmeticGate.evaluate, Cslib.Complexity.Algebraic.ArithmeticCircuit.ext, Cslib.Complexity.Algebraic.ArithmeticCircuit.evaluateNode, Cslib.Complexity.Algebraic.ArithmeticCircuit.evaluate
statement: formalized
proof: formalized
---

# Arithmetic circuits

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html).

## Algebraic

## Arithmetic operand

An arithmetic operand over $F$ with inputs indexed by $A$ and $n$
nodes is a constant $x \in F$, an input $a \in A$, or a reference to a node $i < n$.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticOperand`, an inductive type declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#arithmetic-operand).

## Arithmetic gate

An arithmetic gate over $F$ with inputs indexed by $A$ and $n$ prior
nodes is an addition, a subtraction or a multiplication of two arithmetic operands, each of
which is a constant in $F$, an input $a \in A$ or a reference to a node $i < n$.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticGate`, an inductive type declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#arithmetic-gate).

## Arithmetic circuit

An arithmetic circuit over $F$ with inputs indexed by $A$ and
outputs indexed by $B$ consists of a size $s \in \mathbb{N}$, a gate $g_i$ for each $i < s$, and
an output operand for each $b \in B$. Each gate $g_i$ is an addition, subtraction or
multiplication of two operands, each a constant in $F$, an input $a \in A$ or an earlier gate
$g_j$ with $j < i$; an output operand is a constant in $F$, an input or any gate $g_j$ with
$j < s$.

Constants and inputs are free; each gate counts as one scalar operation.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticCircuit`, a structure declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#arithmetic-circuit).

## Operand evaluation

Let $F$ and $A$ be types and $n \in \mathbb{N}$. Given a value in $F$
for each input $a \in A$ and a value in $F$ for each node $i < n$, an arithmetic operand over $F$
with inputs indexed by $A$ and $n$ nodes evaluates as follows: a constant $x$ evaluates to $x$, an
input $a$ to its assigned value, and a reference to node $i$ to the value given for node $i$.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticOperand.evaluate`, a definition declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#evaluate).

## Gate evaluation

Let $F$ be a type with addition, subtraction and multiplication, let $A$
be a type and let $n \in \mathbb{N}$. Given a value in $F$ for each input $a \in A$ and a value
in $F$ for each node $i < n$, write $v(x)$ for the value of an arithmetic operand $x$: a constant
evaluates to itself, an input $a$ to its assigned value and a reference to node $i$ to the value
given for node $i$. An arithmetic gate over $F$ with inputs indexed by $A$ and $n$ prior nodes
that adds, subtracts or multiplies the operands $x$ and $y$ evaluates to $v(x) + v(y)$,
$v(x) - v(y)$ or $v(x) \cdot v(y)$ respectively.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticGate.evaluate`, a definition declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#evaluate-2).

## Extensionality for arithmetic circuits

Two arithmetic circuits over $F$ with inputs
indexed by $A$ and outputs indexed by $B$ are equal if they have the same size, the same gate at
each position and the same output operand for each $b \in B$.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticCircuit.ext`, a theorem declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#ext).

## Value of a gate in a circuit

Let $F$ be a type with addition, subtraction and
multiplication and let $c$ be an arithmetic circuit over $F$ with inputs indexed by $A$. Given a
value in $F$ for each input $a \in A$, the value of gate $g_i$ of $c$ is the value of the operation
of $g_i$ on its two operands, where a constant $x$ has value $x$, an input has its assigned value
and a reference to an earlier gate $g_j$ with $j < i$ takes the value of $g_j$, defined
recursively.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticCircuit.evaluateNode`, a definition declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#evaluate-node).

## Circuit evaluation

Let $F$ be a type with addition, subtraction and multiplication and
let $c$ be an arithmetic circuit over $F$ with inputs indexed by $A$ and outputs indexed by $B$.
Given a value in $F$ for each input $a \in A$, the value of $c$ at an output $b \in B$ is the value
of the output operand of $b$, where a constant $x$ has value $x$, an input has its assigned value
and a reference to gate $g_j$ has the value of $g_j$, each gate being evaluated from the values of
the gates before it.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticCircuit.evaluate`, a definition declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#evaluate-3).

## Outer-product circuit

For a type $F$ of scalars and $m, n \in \mathbb{N}$, the
outer-product circuit has inputs $a_0, \dots, a_{m-1}$ and $b_0, \dots, b_{n-1}$, one output for
each pair $(i, j)$ with $i < m$ and $j < n$, and exactly $mn$ gates: the gate for $(i, j)$
multiplies $a_i$ by $b_j$, and the output at $(i, j)$ is that gate.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticCircuit.outerProduct`, a definition declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#outer-product).

## Correctness of the outer-product circuit

Let $F$ be a type with addition, subtraction and
multiplication. For all $m, n \in \mathbb{N}$, $a \in F^m$, $b \in F^n$, $i < m$ and $j < n$, the
outer-product circuit over $F$ evaluated on the inputs $a$ and $b$ has value $a_i b_j$ at the
output $(i, j)$.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticCircuit.outerProduct_evaluate`, a theorem declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#outer-product-evaluate).

## Size of the outer-product circuit

For every $F$ and all $m, n \in \mathbb{N}$, the
outer-product circuit over $F$ for $m \times n$ outer products has exactly $mn$ gates.

Formalized by `Cslib.Complexity.Algebraic.ArithmeticCircuit.outerProduct_size`, a theorem declared in [CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/ArithmeticCircuit.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html#outer-product-size).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic circuits](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits)
