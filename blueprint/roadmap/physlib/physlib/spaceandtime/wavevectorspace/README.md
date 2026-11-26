# WaveVectorSpace

The folder [Physlib/SpaceAndTime/WaveVectorSpace/](https://github.com/leanprover-community/physlib/tree/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace): 4 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Wavevector space* ([Physlib/SpaceAndTime/WaveVectorSpace/API-map.md](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Wavevectors and their basic structure
>
> A wavevector is identified by its $d$ real coordinates. [\[1\]](basic.md) Wavevector space has a distinguished zero and is a vector space over the reals: wavevectors may be added, subtracted and multiplied by real numbers. [\[2\]](basic.md) It has both a norm and inner product structure with which it is isometric to standard $d$-dimensional Euclidean space. [\[3\]](basic.md) It has an orthonormal set of basis vectors, and for each basis vector there is a corresponding coordinate function given by orthogonal projection. [\[4\]](basic.md) …
>
> ### Derivatives
>
> Functions from wavevector space into a normed space can be differentiated along the coordinate directions; the partial derivatives satisfy the usual linearity properties, product rule and power rule. [\[5\]](derivatives-basic.md) …
>
> ### Duality with Space
>
> There is a natural pairing of wavevector space with spatial displacements in Space \{1}: for a given wavevector $k$ and point in space $x$ the pairing $k\cdot x = \sum_i k_ix^i$ gives the phase difference relative to some fixed reference point. [\[6\]](dualpairing.md) Fixing a wavevector $k$ gives its dual functional $x \mapsto k\cdot x$ on space and similarly fixing a displacement $x$ gives its dual functional $k \mapsto k\cdot x$ on wavevector space. [\[7\]](dualpairing.md) …
>
> ### Fourier transforms
>
> The Fourier transform (FT) takes a suitably nice function of space to a function of wavevector, resolving its spatial dependence into plane-wave components; the inverse Fourier transform (IFT) reconstructs the spatial function from those components. [\[8\]](fourier.md) Under suitable regularity and integrability assumptions, the FT maps derivatives with respect to space to multiplication by wavevector and *vice versa* [\[9\]](fourier.md) , the FT and IFT are in fact left and right inverses with a consistent choice of normalization \[10\] , and the FT and IFT are continuously differentiable [\[11\]](fourier.md) .

Its references:

> - \{1\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../space/README.md)

- [Wave Vector Space](basic.md)
- [Duality of `Space` and `WaveVectorSpace`](dualpairing.md)
- [Fourier transforms between `Space` and `WaveVectorSpace`](fourier.md)

Modules in [Derivatives/](https://github.com/leanprover-community/physlib/tree/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives):

- [Derivatives on `WaveVectorSpace`](derivatives-basic.md)
