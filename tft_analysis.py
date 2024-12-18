import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Extract: Cargar los datos
def load_data():
    champions_df = pd.read_csv('TFT_Champion_CurrentVersion.csv')
    items_df = pd.read_csv('TFT_Item_CurrentVersion.csv')
    return champions_df, items_df

# Transform: Limpiar y preparar los datos
def transform_data(champions_df):
    # Convertir las columnas de listas en formato string a listas reales
    champions_df['class'] = champions_df['class'].apply(eval)
    
    # Crear columnas adicionales para análisis
    champions_df['num_classes'] = champions_df['class'].apply(len)
    
    return champions_df

# Análisis y Visualización
def analyze_and_visualize(champions_df):
    sns.set_style("whitegrid")
    
    plt.figure(figsize=(10, 6))
    sns.countplot(data=champions_df, x='cost')
    plt.title('Distribución de Costos de Campeones')
    plt.xlabel('Costo')
    plt.ylabel('Cantidad de Campeones')
    plt.savefig('cost_distribution.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=champions_df, x='cost', y='dps')
    plt.title('Relación entre Costo y DPS')
    plt.xlabel('Costo')
    plt.ylabel('DPS')
    plt.savefig('cost_vs_dps.png')
    plt.close()
    
    stats_cols = ['cost', 'health', 'defense', 'attack', 'dps']
    correlation_matrix = champions_df[stats_cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlación de Estadísticas')
    plt.savefig('correlation_matrix.png')
    plt.close()
    
    print("\nTop 10 Campeones por DPS:")
    print(champions_df.nlargest(10, 'dps')[['name', 'dps', 'cost']])
    
    print("\nEstadísticas promedio por costo:")
    print(champions_df.groupby('cost')[['health', 'defense', 'attack', 'dps']].mean())

def main():
    (champions_df, items_df) = load_data()
    
    champions_df = transform_data(champions_df)
    
    analyze_and_visualize(champions_df)

if __name__ == "__main__":
    main()
