---
declaration: section
origin: cited
lean: Cslib.Crypto.MerkleDamgard.chainRev, Cslib.Crypto.MerkleDamgard.chain, Cslib.Crypto.MerkleDamgard.hash, Cslib.Crypto.MerkleDamgard.search, Cslib.Crypto.MerkleDamgard.IsCollision, Cslib.Crypto.MerkleDamgard.findCollision, Cslib.Crypto.MerkleDamgard.findCollision_spec, Cslib.Crypto.MerkleDamgard.hashCollisionGame
statement: formalized
proof: formalized
---

# Merkle–Damgård construction

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html).

## Chaining value of a reversed block list

Let $h : S \times B \to S$ be a compression
function and $iv \in S$ an initial value. The chaining value of a list of blocks given last block
first is defined recursively: the empty list has chaining value $iv$, and a list with first entry
$x$ followed by a list $xs$ has chaining value $h(c, x)$, where $c$ is the chaining value of
$xs$.

Formalized by `Cslib.Crypto.MerkleDamgard.chainRev`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#chain-rev).

## Merkle–Damgård chaining value

Let $h : S \times B \to S$ be a compression function and
$iv \in S$ an initial value. The chaining value of a list of blocks $M = (x_1, \dots, x_L)$ is
$z_L$, where $z_0 = iv$ and $z_i = h(z_{i-1}, x_i)$ for $1 \le i \le L$.

Formalized by `Cslib.Crypto.MerkleDamgard.chain`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#chain).

## Merkle–Damgård hash with length strengthening

Let $h : S \times B \to S$ be a compression
function, $iv \in S$ an initial value and $\ell : \mathbb{N} \to B$ a length encoding. The hash of
a list of blocks $M = (x_1, \dots, x_L)$ is $h(z_L, \ell(L))$, where $z_0 = iv$ and
$z_i = h(z_{i-1}, x_i)$ for $1 \le i \le L$.

Formalized by `Cslib.Crypto.MerkleDamgard.hash`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#hash).

## Backward search for a compression collision

Let $h : S \times B \to S$ be a compression
function with initial value $iv$, and for a list of blocks written last block first let $z(xs)$
be its chaining value: $z([\,]) = iv$ and $z(x :: xs) = h(z(xs), x)$. Given two such lists, the
search compares their leading compression inputs: on $x :: xs$ and $y :: ys$, if
$(z(xs), x) = (z(ys), y)$ it continues with $xs$ and $ys$, and otherwise it returns the pair
$((z(xs), x), (z(ys), y))$. When either list is empty it returns no pair.

Formalized by `Cslib.Crypto.MerkleDamgard.search`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#search).

## Collision of a compression function

Let $h : S \times B \to S$ be a compression function.
A pair $(p_1, p_2)$ of compression inputs in $S \times B$ is a collision of $h$ when $p_1 \ne p_2$
and $h(p_1) = h(p_2)$.

Formalized by `Cslib.Crypto.MerkleDamgard.IsCollision`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#is-collision).

## Extracting a compression collision from a Merkle–Damgård collision

Let
$h : S \times B \to S$ be a compression function, $iv \in S$ an initial value and
$\ell : \mathbb{N} \to B$ a length encoding. Let $M = (x_1, \dots, x_L)$ and
$M' = (x'_1, \dots, x'_{L'})$ be lists of blocks with chaining values $z_0 = z'_0 = iv$,
$z_i = h(z_{i-1}, x_i)$ and $z'_j = h(z'_{j-1}, x'_j)$. The procedure compares the final
compression inputs $(z_L, \ell(L))$ and $(z'_{L'}, \ell(L'))$ and returns this pair if they
differ. Otherwise, for $k = 1, 2, \dots, \min(L, L')$ in turn, it compares
$(z_{L-k}, x_{L-k+1})$ with $(z'_{L'-k}, x'_{L'-k+1})$ and returns the first such pair that
differs; if there is none, it returns no output.

Formalized by `Cslib.Crypto.MerkleDamgard.findCollision`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#find-collision).

## A Merkle–Damgård hash collision yields a compression collision

Let
$h : S \times B \to S$ be a compression function, $iv \in S$ an initial value and
$\ell : \mathbb{N} \to B$ a length encoding, and let $H$ be the Merkle–Damgård hash with length
strengthening they define. Write $|M|$ for the number of blocks of a list of blocks $M$. If $M$
and $M'$ are distinct lists of blocks with $H(M) = H(M')$, and $\ell(|M|) = \ell(|M'|)$ implies
$|M| = |M'|$, then the collision-finding procedure applied to $M$ and $M'$ returns a pair
$(p_1, p_2)$ of compression inputs with $p_1 \ne p_2$ and $h(p_1) = h(p_2)$.

This is a block-level form of Katz and Lindell, Theorem 5.4.

Formalized by `Cslib.Crypto.MerkleDamgard.findCollision_spec`, a theorem declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#find-collision-spec).

## Hash collision game for Merkle–Damgård

Let $H$ be the Merkle–Damgård hash with length
strengthening defined by a compression function $h : S \times B \to S$, an initial value
$iv \in S$ and a length encoding $\ell : \mathbb{N} \to B$, and let $N$ be a natural number. An
adversary $A$ maps random coins $r$ from a finite nonempty type $R$ to a pair of lists of blocks.
The game is the distribution of the Boolean outcome when $r$ is drawn uniformly from $R$: the
adversary wins (outcome true) exactly when $A(r) = (M, M')$ with $M \ne M'$, both $M$ and $M'$
have fewer than $N$ blocks, and $H(M) = H(M')$.

Formalized by `Cslib.Crypto.MerkleDamgard.hashCollisionGame`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#hash-collision-game).

## Compression-function collision game

Let $h : S \times B \to S$ be a compression function
and let $A$ be an adversary that maps random coins $r$ from a finite nonempty type $R$ either to a
pair $(p_1, p_2)$ of compression inputs in $S \times B$ or to no output. The game is the
distribution of the Boolean outcome when $r$ is drawn uniformly from $R$: the adversary wins
(outcome true) exactly when $A(r)$ is a pair $(p_1, p_2)$ with $p_1 \ne p_2$ and
$h(p_1) = h(p_2)$, and loses when $A(r)$ is no output.

Formalized by `Cslib.Crypto.MerkleDamgard.compressionCollisionGame`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#compression-collision-game).

## Merkle–Damgård collision reduction

Let $h : S \times B \to S$ be a compression function,
$iv \in S$ an initial value, $\ell : \mathbb{N} \to B$ a length encoding and $A$ an adversary that
maps random coins $r$ from a finite nonempty type $R$ to a pair $(M, M')$ of lists of blocks. The
reduction is the adversary that, on coins $r$, outputs the result of the Merkle–Damgård
collision-finding procedure applied to the pair $(M, M') = A(r)$: a pair of compression inputs,
or no output.

Formalized by `Cslib.Crypto.MerkleDamgard.reduction`, a definition declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#reduction).

## The Merkle–Damgård transform preserves collision resistance

Let $h : S \times B \to S$
be a compression function, $iv \in S$ an initial value, $\ell : \mathbb{N} \to B$ a length
encoding and $N$ a natural number such that $\ell$ is injective on $\{0, 1, \dots, N - 1\}$. Then
for every adversary $A$ that maps random coins from a finite nonempty type $R$ to a pair of lists
of blocks, the probability that the reduction built from $A$ wins the compression-function
collision game for $h$ is at least the probability that $A$ wins the hash collision game for the
Merkle–Damgård hash defined by $h$, $iv$ and $\ell$ with messages of fewer than $N$ blocks.

Formalized by `Cslib.Crypto.MerkleDamgard.hashCollisionGame_le`, a theorem declared in [CSLibExt/Crypto/Hash/MerkleDamgard.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/Hash/MerkleDamgard.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html#hash-collision-game-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Merkle–Damgård construction](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/cryptography/hash-functions/merkle-damg-rd-construction)
