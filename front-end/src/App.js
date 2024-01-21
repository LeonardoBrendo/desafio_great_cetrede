
import React, { useState, useEffect } from 'react';
import './App.css';

const App = () => {
  const [uf, setUF] = useState('SP');
  const [codigoUF, setCodigoUF] = useState('');
  const [nomeCidade, setNomeCidade] = useState('');
  const [escolas, setEscolas] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 10;

  useEffect(() => {
    const fetchData = async () => {
      try {
        let endpoint = '';

        if (uf) {
          endpoint = `http://localhost:5000/api/escolas_sguf/${uf}`;
        } else if (codigoUF) {
          endpoint = `http://localhost:5000/api/escolas_couf/${codigoUF}`;
        } else if (nomeCidade) {
          endpoint = `http://localhost:5000/api/escolas_cidade/${nomeCidade}`;
        } else {
          // Se nenhum filtro for aplicado, buscar todas as escolas
          endpoint = 'http://localhost:5000/api/escolas';
        }

        const response = await fetch(endpoint);
        if (!response.ok) {
          throw new Error('Erro ao buscar dados');
        }
        const data = await response.json();

        if (Array.isArray(data)) {
          setEscolas(data);
        } else {
          console.error('Resposta inválida da API:', data);
        }
      } catch (error) {
        console.error('Erro:', error);
      }
    };

    fetchData();
  }, [uf, codigoUF, nomeCidade]);

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = escolas.slice(indexOfFirstItem, indexOfLastItem);

  const totalPages = Math.ceil(escolas.length / itemsPerPage);

  const handlePageChange = (newPage) => {
    if (newPage >= 1 && newPage <= totalPages) {
      setCurrentPage(newPage);
    }
  };

  return (
    <div className='background-container'>
      <h1>INFORMAÇÕES DAS ESCOLAS DA FEDERAÇÃO BRASILEIRA</h1>

      <label>
        Filtrar por nome do estado:
        <select
          value={uf}
          onChange={(e) => setUF(e.target.value)}
        >
          <option value="AC">Acre</option>
          <option value="AL">Alagoas</option>
          <option value="AP">Amapá</option>
          <option value="AM">Amazonas</option>
          <option value="BA">Bahia</option>
          <option value="CE">Ceará</option>
          <option value="DF">Distrito Federal</option>
          <option value="ES">Espírito Santo</option>
          <option value="GO">Goiás</option>
          <option value="MA">Maranhão</option>
          <option value="MT">Mato Grosso</option>
          <option value="MS">Mato Grosso do Sul</option>
          <option value="MG">Minas Gerais</option>
          <option value="PA">Pará</option>
          <option value="PB">Paraíba</option>
          <option value="PR">Paraná</option>
          <option value="PE">Pernambuco</option>
          <option value="PI">Piauí</option>
          <option value="RJ">Rio de Janeiro</option>
          <option value="RN">Rio Grande do Norte</option>
          <option value="RS">Rio Grande do Sul</option>
          <option value="RO">Rondônia</option>
          <option value="RR">Roraima</option>
          <option value="SC">Santa Catarina</option>
          <option value="SP">São Paulo</option>
          <option value="SE">Sergipe</option>
          <option value="TO">Tocantis</option>          
          {/* Adicione outras opções de estados conforme necessário */}
        </select>
      </label>

      {/* <label>
        Filtrar por código do estado:
        <select
          value={codigoUF}
          onChange={(e) => setCodigoUF(e.target.value)}
        >
          <option value="12">12 - Acre</option>
          <option value="27">27 -Alagoas</option>
          <option value="AP">Amapá</option>
          <option value="AM">Amazonas</option>
          <option value="BA">Bahia</option>
          <option value="CE">Ceará</option>
          <option value="DF">Distrito Federal</option>
          <option value="ES">Espírito Santo</option>
          <option value="GO">Goiás</option>
          <option value="MA">Maranhão</option>
          <option value="MT">Mato Grosso</option>
          <option value="MS">Mato Grosso do Sul</option>
          <option value="MG">Minas Gerais</option>
          <option value="PA">Pará</option>
          <option value="PB">Paraíba</option>
          <option value="PR">Paraná</option>
          <option value="PE">Pernambuco</option>
          <option value="PI">Piauí</option>
          <option value="RJ">Rio de Janeiro</option>
          <option value="RN">Rio Grande do Norte</option>
          <option value="RS">Rio Grande do Sul</option>
          <option value="RO">Rondônia</option>
          <option value="RR">Roraima</option>
          <option value="SC">Santa Catarina</option>
          <option value="SP">São Paulo</option>
          <option value="SE">Sergipe</option>
          <option value="TO">Tocantis</option>
        </select>
      </label> */}

      {/* <label>
        Filtrar por nome da cidade:
        <input
          type="text"
          value={nomeCidade}
          onChange={(e) => setNomeCidade(e.target.value)}
        />
      </label> */}

      <table className="school-table">
        <thead>
          <tr>
            {Object.keys(currentItems[0] || {}).map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {currentItems.map((escola) => (
            <tr key={escola.ID_ESCOLA}>
              {Object.values(escola).map((value) => (
                <td key={value}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      <div className="pagination">
        <button onClick={() => handlePageChange(1)}>&#171;</button> {/* Seta para a esquerda */}
        <button onClick={() => handlePageChange(currentPage - 1)} disabled={currentPage === 1}>&lt;</button> {/* Seta para a esquerda */}
        <span>{currentPage}</span>
        <button onClick={() => handlePageChange(currentPage + 1)} disabled={currentPage === totalPages}>&gt;</button> {/* Seta para a direita */}
        <button onClick={() => handlePageChange(totalPages)}>&#187;</button> {/* Seta para a direita */}
      </div>
    </div>
  );
};

export default App;
