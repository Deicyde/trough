---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.initState, MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.QMAPromise, MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.PromiseReduces, MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.LocalTerm, MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.embedTerm, MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.hamiltonian, MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.groundEnergy, MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.localTermValid
statement: formalized
---

# Local Hamiltonian problem

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html).

## Initial state of a QMA verifier

For a bitstring $x = (x_0, \dots, x_{n-1})$, with true
read as $1$ and false as $0$, numbers $m$ and $a$, and a vector $\psi \in \mathbb{C}^{2^m}$ (the
witness on $m$ qubits), the initial state is the tensor product of the computational basis state
of $x$, the vector $\psi$ and the all-zero state on $a$ ancilla qubits, in this order. It is the
vector on $\{0, \dots, 2^{n+m+a} - 1\}$ whose value at $s$ is $\psi(\lfloor s / 2^n \rfloor)$ if
$s < 2^{n+m}$ and $s \bmod 2^n = \sum_{k < n} x_k 2^k$, and $0$ otherwise. So $x$ occupies the
$n$ low-order bits of the index, the witness the next $m$ bits and the ancillas the $a$
high-order bits.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.initState`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#init-state).

## QMA for promise problems

A pair $(\Pi_{\mathrm{yes}}, \Pi_{\mathrm{no}})$ of sets of
bitstrings is in QMA when there are polynomials $m$, $a$ and $s$ with natural-number coefficients
and a polynomial-time computable map sending each bitstring $x$ to a list of encoded 2-local
quantum gates such that, for every bitstring $x$, writing $N = |x| + m(|x|) + a(|x|)$: the list
has at most $s(|x|)$ gates, each well-formed on $N$ qubits; if $x \in \Pi_{\mathrm{yes}}$, some
state $\psi$ on $m(|x|)$ qubits with squared norm $1$ makes the acceptance probability of the
circuit, applied to the tensor product of the basis state of $x$, $\psi$ and the all-zero state
on $a(|x|)$ qubits, at least $2/3$; and if $x \in \Pi_{\mathrm{no}}$, every state $\psi$ on
$m(|x|)$ qubits with squared norm $1$ makes this acceptance probability at most $1/3$.

No condition is imposed on bitstrings outside $\Pi_{\mathrm{yes}} \cup \Pi_{\mathrm{no}}$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.QMAPromise`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#qmapromise).

## Polynomial-time reduction between promise problems

A promise problem $(Y_1, N_1)$,
given by sets $Y_1$ and $N_1$ of bitstrings, reduces to another such promise problem $(Y_2, N_2)$
when there is a polynomial-time computable map $f$ from bitstrings to bitstrings with
$f(x) \in Y_2$ for every $x \in Y_1$ and $f(x) \in N_2$ for every $x \in N_1$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.PromiseReduces`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#promise-reduces).

## Encoded 2-local Hamiltonian term

A 2-local Hamiltonian term is encoded as a triple
$(i, j, e)$ of natural numbers $i$ and $j$, the qubits it acts on, and a list $e$ of pairs of
encoded rational numbers, the real and imaginary parts of the entries of its $4 \times 4$ matrix
in row-major order.

The encoding itself does not require $e$ to have $16$ entries or the matrix to be Hermitian; the
qubit bounds, the number of entries and positive semidefiniteness (hence Hermiticity) are part of
the validity of a term.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.LocalTerm`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#local-term).

## Embedding of a 2-local term into $n$ qubits

Let a 2-local term act on qubits $i$ and $j$,
and let $M$ be the $4 \times 4$ complex matrix encoded by its list of entries, with rows and
columns indexed by pairs of bits. Its embedding into $n$ qubits is the $2^n \times 2^n$ complex
matrix whose entry at basis indices $s, t \in \{0, \dots, 2^n - 1\}$ is
$M_{(s_i, s_j), (t_i, t_j)}$ if $s_k = t_k$ for every $k \ne i, j$, and $0$ otherwise, where
$s_k = \lfloor s / 2^k \rfloor \bmod 2$ is bit $k$ of $s$.

When $i \ne j$ and $i, j < n$, this is $M$ acting on qubits $i$ and $j$, tensored with the
identity on the other qubits.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.embedTerm`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#embed-term).

## Hamiltonian of a list of 2-local terms

For a number $n$ of qubits and a list
$h_1, \dots, h_m$ of 2-local terms, the Hamiltonian is the $2^n \times 2^n$ complex matrix
$\tilde h_1 + \dots + \tilde h_m$, where $\tilde h_l$ is the embedding of $h_l$ into $n$ qubits;
for the empty list it is the zero matrix.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.hamiltonian`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#hamiltonian).

## Ground energy of a Hermitian matrix

For a natural number $n$, the ground energy of a
Hermitian $2^n \times 2^n$ complex matrix $H$ is the smallest eigenvalue of $H$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.groundEnergy`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#ground-energy).

## Valid 2-local Hamiltonian term

A 2-local term acting on qubits $i$ and $j$ with entry
list $e$ is valid on $n$ qubits when $i < j < n$, the list $e$ has exactly $16$ entries, each
entry has nonzero denominators in the encodings of both its real and its imaginary part, the
$4 \times 4$ complex matrix $M$ encoded by $e$ is positive semidefinite, and
$\sum_{p, q} |M_{pq}|^2 \le 1$, that is, $M$ has Frobenius norm at most $1$.

In particular $M$ is Hermitian and has operator norm at most $1$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.localTermValid`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#local-term-valid).

## Yes-instances of the 2-local Hamiltonian problem

A bitstring $x$ is a yes-instance when
decoding it under the canonical bitstring encoding gives a tuple $(n, (h_1, \dots, h_m), a, b)$ of
a natural number $n$, a list of 2-local terms $h_1, \dots, h_m$ and two encoded rational numbers,
whose values we also write $a$ and $b$, such that every $h_l$ is valid on $n$ qubits,
$b - a \ge 1/(m + 1)$, and the Hamiltonian $H$ of $h_1, \dots, h_m$ on $n$ qubits is Hermitian
and has ground energy at most $a$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.LocalHamYes`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#local-ham-yes).

## No-instances of the 2-local Hamiltonian problem

A bitstring $x$ is a no-instance when
decoding it under the canonical bitstring encoding gives a tuple $(n, (h_1, \dots, h_m), a, b)$ of
a natural number $n$, a list of 2-local terms $h_1, \dots, h_m$ and two encoded rational numbers,
whose values we also write $a$ and $b$, such that every $h_l$ is valid on $n$ qubits,
$b - a \ge 1/(m + 1)$, and the Hamiltonian $H$ of $h_1, \dots, h_m$ on $n$ qubits is Hermitian
and has ground energy at least $b$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.LocalHamNo`, a definition declared in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#local-ham-no).

## The 2-local Hamiltonian problem is QMA-complete

The 2-local Hamiltonian promise
problem, given by its yes-instances and no-instances, is in QMA, and every promise problem in QMA
whose sets of yes-instances and no-instances are disjoint sets of bitstrings has a polynomial-time
reduction to it.

Here an instance encodes a number $n$ of qubits, a list of $m$ valid 2-local terms on $n$ qubits
and encoded rationals $a$ and $b$ with $b - a \ge 1/(m + 1)$; it is a yes-instance when the
Hamiltonian of the terms on $n$ qubits is Hermitian with ground energy at most $a$, and a
no-instance when it is Hermitian with ground energy at least $b$.

## Sources

- A. Y. Kitaev, "Quantum NP", talk at AQIP 1999; A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4; J. Kempe, A. Y. Kitaev, and O. Regev, "The complexity of the local Hamiltonian problem", SIAM Journal on Computing 35 (2006), 1070-1097 (the 2-local reduction); A. D. Bookatz, "QMA-complete problems", arXiv:1212.6312 (2012), Section 2 (survey of the QMA-completeness of the local Hamiltonian problem); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 10, for the QMA-completeness of 2-local Hamiltonian.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.LocalHamiltonianQMA.local_hamiltonian_qma_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/LocalHamiltonianQMAWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html#local-hamiltonian-qma-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local Hamiltonian problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/local-hamiltonian-problem)
